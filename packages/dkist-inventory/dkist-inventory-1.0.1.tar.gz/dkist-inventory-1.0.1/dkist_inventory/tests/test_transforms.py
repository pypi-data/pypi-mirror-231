import numpy as np
import pytest

import astropy.units as u
import gwcs.coordinate_frames as cf
from astropy.io import fits
from astropy.modeling import Model, models
from astropy.time import Time

from dkist_inventory.header_parsing import HeaderParser
from dkist_inventory.transforms import (
    linear_spectral_model,
    linear_time_model,
    spatial_model_from_header,
    spectral_model_from_framewave,
    time_model_from_date_obs,
    TransformBuilder
)


@pytest.fixture
def wcs(transform_builder):
    return transform_builder.gwcs


@pytest.fixture
def non_varying_wcs(non_varying_transform_builder):
    return non_varying_transform_builder.gwcs


def test_transform(transform_builder):
    assert isinstance(transform_builder.transform, Model)


def test_frames(transform_builder):
    frames = transform_builder.frames
    assert all([isinstance(frame, cf.CoordinateFrame) for frame in frames])


def test_input_name_ordering(transform_builder):
    # Check the ordering of the input and output frames
    wcs = transform_builder.gwcs
    allowed_pixel_names = {
        "VISP": (
            ("slit position", "wavelength", "raster position", "scan number"),
            ("slit position", "wavelength", "raster position", "scan number", "stokes"),
            ("slit position", "wavelength", "raster position"),
            ("slit position", "wavelength", "raster position", "stokes"),
            ("wavelength", "slit position", "raster position", "scan number"),
            ("wavelength", "slit position", "raster position", "scan number", "stokes"),
            ("wavelength", "slit position", "raster position"),
            ("wavelength", "slit position", "raster position", "stokes"),
        ),
        "VTF": (
            ("spatial x", "spatial y", "scan position", "scan repeat number", "stokes"),
            ("spatial x", "spatial y", "scan position", "scan repeat number"),
            ("spatial x", "spatial y", "scan position"),
        ),
        "VBI": (
            ("spatial x", "spatial y", "frame number"),
        ),
        "CRYO-NIRSP": (
            # SP
            ("dispersion axis", "spatial along slit", "map scan step number", "scan number", "stokes"),
            ("dispersion axis", "spatial along slit", "map scan step number", "scan number"),
            ("dispersion axis", "spatial along slit", "measurement number", "map scan step number", "scan number", "stokes"),
            ("dispersion axis", "spatial along slit", "measurement number", "map scan step number", "scan number"),
            # CI
            ("helioprojective latitude", "helioprojective longitude", "map scan step number", "scan number", "stokes"),
            ("helioprojective latitude", "helioprojective longitude", "map scan step number", "scan number"),
            ("helioprojective latitude", "helioprojective longitude", "measurement number", "map scan step number", "scan number", "stokes"),
            ("helioprojective latitude", "helioprojective longitude", "measurement number", "map scan step number", "scan number"),
        )

    }
    assert wcs.input_frame.axes_names in allowed_pixel_names[transform_builder.header["INSTRUME"]]


def test_output_name_ordering(transform_builder):
    wcs = transform_builder.gwcs

    allowed_world_names = {
        "VISP": (
            # These are split to correspond to the order of the `_values`
            # numbers not the high level objects.
            ("helioprojective latitude", "wavelength", "helioprojective longitude", "time"),
            ("helioprojective latitude", "wavelength", "helioprojective longitude", "time", "stokes"),
            ("wavelength", "helioprojective latitude", "helioprojective longitude", "time"),
            ("wavelength", "helioprojective latitude", "helioprojective longitude", "time",
             "stokes"),
        ),
        "VTF": (
            ("helioprojective longitude", "helioprojective latitude", "wavelength", "time", "stokes"),
            ("helioprojective longitude", "helioprojective latitude", "wavelength", "time"),
        ),
        "VBI": (
            ("helioprojective longitude", "helioprojective latitude", "time"),
        ),
        "CRYO-NIRSP": (
            # SP
            ("wavelength", "helioprojective longitude", "helioprojective latitude", "time"),
            ("wavelength", "helioprojective longitude", "helioprojective latitude", "time", "stokes"),
            # TODO: Makes me wonder if we should use set comparison instead...
            # If multi-meas are present (time), they come before latitude
            ("wavelength", "helioprojective longitude", "time", "helioprojective latitude"),
            ("wavelength", "helioprojective longitude", "time", "helioprojective latitude", "stokes"),
            # CI
            ("helioprojective latitude", "helioprojective longitude", "time"),
            ("helioprojective latitude", "helioprojective longitude", "time", "stokes"),
        )
    }

    assert wcs.output_frame.axes_names in allowed_world_names[transform_builder.header["INSTRUME"]]


def test_output_frames(transform_builder):
    wcs = transform_builder.gwcs
    allowed_frame_orders = {
        "VISP": (
            (cf.CelestialFrame, cf.SpectralFrame, cf.TemporalFrame, cf.StokesFrame),
            (cf.CelestialFrame, cf.SpectralFrame, cf.TemporalFrame),
            (cf.SpectralFrame, cf.CelestialFrame, cf.TemporalFrame, cf.StokesFrame),
            (cf.SpectralFrame, cf.CelestialFrame, cf.TemporalFrame),
        ),
        "VTF": (
            (cf.CelestialFrame, cf.SpectralFrame, cf.TemporalFrame, cf.StokesFrame),
            (cf.CelestialFrame, cf.SpectralFrame, cf.TemporalFrame),
        ),
        "VBI": (
            (cf.CelestialFrame, cf.TemporalFrame),
        ),
        "CRYO-NIRSP": (
            # SP
            (cf.SpectralFrame, cf.CelestialFrame, cf.TemporalFrame, cf.StokesFrame),
            (cf.SpectralFrame, cf.CelestialFrame, cf.TemporalFrame),
            #CI
            (cf.CelestialFrame, cf.TemporalFrame, cf.StokesFrame),
            (cf.CelestialFrame, cf.TemporalFrame),
        )
            }
    types = tuple((type(frame) for frame in wcs.output_frame.frames))
    assert types in allowed_frame_orders[transform_builder.header["INSTRUME"]]


def test_transform_models(non_varying_wcs):
    # Test that there is one lookup table and two linear models for both the
    # wcses
    sms = non_varying_wcs.forward_transform._leaflist
    smtypes = [type(m) for m in sms]
    if len(smtypes) == 4:  # VTF and VISP
        assert sum(mt is models.Linear1D for mt in smtypes) == 2
        assert sum(mt is models.Tabular1D for mt in smtypes) == 1
    if len(smtypes) == 2:  # VBI
        assert sum(mt is models.Linear1D for mt in smtypes) == 1


def first_header(header_filenames):
    return fits.getheader(header_filenames[0])


def test_spatial_model(header_filenames):
    sampling, spatial = spatial_model_from_header(first_header(header_filenames))
    assert isinstance(spatial, Model)


def test_linear_spectral():
    lin = linear_spectral_model(10 * u.nm, 0 * u.nm)
    assert isinstance(lin, models.Linear1D)
    assert u.allclose(lin.slope, 10 * u.nm / u.pix)
    assert u.allclose(lin.intercept, 0 * u.nm)


def test_linear_time():
    lin = linear_time_model(10 * u.s)
    assert isinstance(lin, models.Linear1D)
    assert u.allclose(lin.slope, 10 * u.s / u.pix)
    assert u.allclose(lin.intercept, 0 * u.s)


@pytest.mark.parametrize("dataset_name", ["vbi"])
def test_time_from_dateobs(dataset_name, simulated_dataset):
    directory = simulated_dataset(dataset_name)
    header_filenames = directory.glob("*")
    date_obs = [fits.getheader(f)["DATE-BEG"] for f in header_filenames]
    date_obs.sort()
    delta = Time(date_obs[1]) - Time(date_obs[0])
    sampling, time = time_model_from_date_obs(np.array(date_obs))
    assert isinstance(time, models.Linear1D)
    np.testing.assert_allclose(time.slope, delta.to(u.s) / (1 * u.pix))


def test_time_from_dateobs_lookup(header_filenames):
    date_obs = [fits.getheader(f)["DATE-BEG"] for f in header_filenames]
    date_obs[3] = (Time(date_obs[3]) + 10 * u.s).isot
    deltas = Time(date_obs) - Time(date_obs[0])
    sampling, time = time_model_from_date_obs(np.array(date_obs))
    assert isinstance(time, models.Tabular1D)
    assert (time.lookup_table == deltas.to(u.s)).all()
    np.testing.assert_allclose(time.lookup_table, deltas.to(u.s))


def test_spectral_framewave(header_filenames):
    head = first_header(header_filenames)

    # Skip the VISP headers
    if "FRAMEWAV" not in head:
        return

    nwave = head["DNAXIS3"]
    framewave = [fits.getheader(h)["FRAMEWAV"] for h in header_filenames]

    sampling, m = spectral_model_from_framewave(framewave[:nwave])
    assert isinstance(m, models.Linear1D)

    sampling, m2 = spectral_model_from_framewave(framewave)
    assert isinstance(m2, models.Tabular1D)


def test_time_varying_vbi_wcs(vbi_time_varying_transform_builder):
    if not hasattr(Model, "_calculate_separability_matrix"):
        pytest.skip()
    wcs = vbi_time_varying_transform_builder.gwcs
    assert np.allclose(wcs.axis_correlation_matrix,
                       np.array([[True,  True,  True],  # noqa
                                 [True,  True,  True],  # noqa
                                 [False, False, True]]))


def test_non_time_varying_vtf(dataset):
    ds = dataset("vtf")
    wcs = TransformBuilder(HeaderParser.from_headers(ds.generate_headers())).gwcs
    assert wcs.forward_transform.n_inputs == 5


def test_split_visp_matrix(dataset):
    """
    Given:
        A VISP dataset where the spatial pixel axes are not next to each
        other and there is no need to duplicate pixel inputs to the transform
    Then:
        Generate a WCS
    Assert:
        The axis correlation matrix matches the expected matrix
    """
    ds = dataset("visp-time-varying-single")
    header_parser = HeaderParser.from_headers(ds.generate_headers())
    builder = TransformBuilder(header_parser)
    wcs = builder.gwcs

    # This test case is Stokes I only, one map scan, 4 raster steps.
    # We have 3 pixel axes: slit_y, disperson, raster
    # and 4 world axes: lat, lon, wave, time
    # Time varies along the raster dimension
    # lat and lon vary along slit_y and also raster
    # wave varies along dispersion

    # Remember that the correlation matrix is (world, pixel)
    # i.e. rows are world axes, cols are pixel axes
    assert np.allclose(wcs.axis_correlation_matrix,
                       [[ True, False,  True],
                        [False,  True, False],
                        [ True, False,  True],
                        [False, False,  True]]
                       )


def test_split_visp_matrix_dupe(dataset):
    """
    Given:
        A VISP dataset where the spatial pixel axes are not next to each
        other and there is a need to duplicate pixel inputs to the transform
    Then:
        Generate a WCS
    Assert:
        The axis correlation matrix matches the expected matrix
    """
    ds = dataset("visp")
    header_parser = HeaderParser.from_headers(ds.generate_headers())
    builder = TransformBuilder(header_parser)
    wcs = builder.gwcs

    # This test case is full stokes, two map scans, 2 raster steps.
    # We have 5 pixel axes: slit_y, disperson, raster, scan number, stokes
    # and 5 world axes: lat, lon, wave, time, stokes
    # Time varies along the raster dimension and the scan number dimension
    # lat and lon vary along slit_y and raster (not scan number as this has a fixed pointing)
    # wave varies along dispersion

    # Remember that the correlation matrix is (world, pixel)
    # i.e. rows are world axes, cols are pixel axes
    assert np.allclose(wcs.axis_correlation_matrix,
                       [[ True, False,  True, False, False],
                        [False,  True, False, False, False],
                        [ True, False,  True, False, False],
                        [False, False,  True,  True, False],
                        [False, False, False, False,  True]]
                       )
