import pytest
from eth_utils import decode_hex
from mythril.laser.ethereum.natives import mod_exp
from ethereum.utils import big_endian_to_int


EIP198_VECTOR_A = decode_hex(
    "0000000000000000000000000000000000000000000000000000000000000001"
    "0000000000000000000000000000000000000000000000000000000000000020"
    "0000000000000000000000000000000000000000000000000000000000000020"
    "03"
    "fffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2e"
    "fffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f"
)

EIP198_VECTOR_B = decode_hex(
    "0000000000000000000000000000000000000000000000000000000000000000"
    "0000000000000000000000000000000000000000000000000000000000000020"
    "0000000000000000000000000000000000000000000000000000000000000020"
    "fffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2e"
    "fffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f"
)

EIP198_VECTOR_C = decode_hex(
    "0000000000000000000000000000000000000000000000000000000000000001"
    "0000000000000000000000000000000000000000000000000000000000000002"
    "0000000000000000000000000000000000000000000000000000000000000020"
    "03"
    "ffff"
    "8000000000000000000000000000000000000000000000000000000000000000"
    "07"
)

EIP198_VECTOR_D = decode_hex(
    "0000000000000000000000000000000000000000000000000000000000000001"
    "0000000000000000000000000000000000000000000000000000000000000002"
    "0000000000000000000000000000000000000000000000000000000000000020"
    "03"
    "ffff"
    "80"
)


@pytest.mark.parametrize(
    "data,expected",
    (
        (EIP198_VECTOR_A, 1),
        (EIP198_VECTOR_B, 0),
        (
            EIP198_VECTOR_C,
            26689440342447178617115869845918039756797228267049433585260346420242739014315,
        ),
        (
            EIP198_VECTOR_D,
            26689440342447178617115869845918039756797228267049433585260346420242739014315,
        ),
    ),
)
def test_modexp_result(data, expected):
    actual = mod_exp(data)
    assert big_endian_to_int(actual) == expected
