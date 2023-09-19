from typing import Tuple

# Define constants relating to the default/current version of System Coupling

SYC_MAJOR_VERSION = 24
SYC_MINOR_VERSION = 1

SYC_VERSION_CONCAT = f"{SYC_MAJOR_VERSION}{SYC_MINOR_VERSION}"
SYC_VERSION_DOT = f"{SYC_MAJOR_VERSION}.{SYC_MINOR_VERSION}"
SYC_VERSION_UNDERSCORE = f"{SYC_MAJOR_VERSION}_{SYC_MINOR_VERSION}"


def normalize_version(version: str) -> Tuple[int, int]:
    """Utility to convert a version string provided in a number of
    possible formats into pair of ints representing the major and minor version
    numbers.

    .. note::
        The current implementation only supports simple major-minor version
        strings, containing three digits in various configurations(two digits
        for major version, one for minor).

    Parameters
    ----------
    version : str
        Version string in one of the three formats, "23.1", "23_1", or "231".
        Given any of these example strings, the return value would be (23, 1).
    """

    def raise_error():
        raise ValueError(f"Version string {version} in unsupported format.")

    def split_at_separator(sep: str) -> Tuple[int, int]:
        if sep not in version:
            return None
        components = version.split(sep)
        if len(components) != 2 or not (
            len(components[0]) == 2 and len(components[1]) == 1
        ):
            raise_error()
        return process_major_minor(components[0], components[1])

    def process_major_minor(major_str: str, minor_str: str) -> Tuple[int, int]:
        try:
            major = int(major_str)
            minor = int(minor_str)
            return (major, minor)
        except:
            raise_error()

    ret = split_at_separator(".") or split_at_separator("_")
    if ret is not None:
        return ret

    if len(version) == 3:
        return process_major_minor(version[0:2], version[2])
    else:
        raise_error()


def compare_versions(version_a: str, version_b: str) -> int:
    """Compares two version strings that are in any form that can be parsed by
    ``normalize_version``.

    Returns < 0 if ``version_a`` is an earlier version than ``version_b``, 0
    if they are the same version, and > 0 if ``version_a`` is a later version
    than ``version_b``.

    Parameters
    ----------
    version_a : str
        The first version string to compare.
    version_b: str
        The second version string to compare.
    """
    va_maj, va_min = normalize_version(version_a)
    vb_maj, vb_min = normalize_version(version_b)

    if va_maj == vb_maj:
        return va_min - vb_min
    else:
        return va_maj - vb_maj
