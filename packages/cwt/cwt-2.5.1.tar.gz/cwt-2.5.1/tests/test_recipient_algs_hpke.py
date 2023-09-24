"""
Tests for HPKE.
"""

import pytest

from cwt.recipient_algs.hpke import HPKE


class TestHPKE:
    """
    Tests for HPKE.
    """

    def test_recipient_algs_hpke(self):
        ctx = HPKE({1: -1}, {-4: [0x0010, 0x0001, 0x0001]})
        assert isinstance(ctx, HPKE)
        assert ctx.alg == -1

    def test_recipient_algs_hpke_without_alg(self):
        with pytest.raises(ValueError) as err:
            HPKE({1: 1}, {-4: [0x0010, 0x0001, 0x0001]})
            pytest.fail("HPKE should fail.")
        assert "alg should be HPKE(-1)." in str(err.value)

    @pytest.mark.parametrize(
        "hsi, msg",
        [
            (
                {},
                "HPKE sender information(-4) not found.",
            ),
            (
                {-4: [0x0001]},
                "HPKE sender information(-4) should be a list of length 3 or 4.",
            ),
            (
                {-4: [0x0001, 0x0001]},
                "HPKE sender information(-4) should be a list of length 3 or 4.",
            ),
            (
                {-4: {1: 0x0010, 3: 0x0001}},
                "HPKE sender information(-4) should be a list of length 3 or 4.",
            ),
            (
                {-4: {1: 0x0010, 2: 0x0001}},
                "HPKE sender information(-4) should be a list of length 3 or 4.",
            ),
            (
                {-4: [0xFFFF, 0x0001, 0x0001]},
                "65535 is not a valid KEMId",
            ),
            (
                {-4: [0x0010, 0xFFFF, 0x0001]},
                "65535 is not a valid KDFId",
            ),
            (
                {-4: [0x0010, 0x0001, 0xFFFE]},
                "65534 is not a valid AEADId",
            ),
        ],
    )
    def test_recipient_algs_hpke_with_invalid_hsi(self, hsi, msg):
        with pytest.raises(ValueError) as err:
            HPKE({1: -1}, hsi)
            pytest.fail("HPKE should fail.")
        assert msg in str(err.value)
