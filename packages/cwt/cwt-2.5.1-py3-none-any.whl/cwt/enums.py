import enum


class COSETypes(enum.IntEnum):
    ENCRYPT0 = 1
    ENCRYPT = 2
    MAC0 = 3
    MAC = 4
    SIGN1 = 5
    SIGN = 6
    COUNTERSIGNATURE = 7
    RECIPIENT = 8
    SIGNATURE = 9


class COSEHeaders(enum.IntEnum):
    HPKE_SENDER_INFO = -4
    ALG = 1
    CRIT = 2
    CTY = 3
    KID = 4
    IV = 5
    PARTIAL_IV = 6
    COUNTER_SIGNATURE = 7
    COUNTER_SIGNATURE_0 = 9
    KID_CONTEXT = 10
    COUNTER_SIGNATURE_V2 = 11
    COUNTER_SIGNATURE_0_V2 = 12
    CWT_CLAIMS = 13
    X5BAG = 32
    X5CHAIN = 33
    X5T = 34
    X5U = 35
    CUPH_NONCE = 256
    CUPH_OWNER_PUB_KEY = 257


class COSEKeyParams(enum.IntEnum):
    KTY = 1
    KID = 2
    ALG = 3
    KEY_OPS = 4
    BASE_IV = 5
    CRV = -1
    X = -2
    Y = -3
    D = -4
    RSA_N = -1
    RSA_E = -2
    RSA_D = -3
    RSA_P = -4
    RSA_Q = -5
    RSA_DP = -6
    RSA_DQ = -7
    RSA_QINV = -8
    RSA_OTHER = -9
    RSA_R_I = -10
    RsA_D_I = -11
    RSA_T_I = -12
    K = -1


class COSEAlgs(enum.IntEnum):
    RS512 = -259
    RS384 = -258
    RS256 = -257
    ES256K = -47
    PS512 = -39
    PS384 = -38
    PS256 = -37
    ES512 = -36
    ES384 = -35
    ECDH_SS_A256KW = -34
    ECDH_SS_A192KW = -33
    ECDH_SS_A128KW = -32
    ECDH_ES_A256KW = -31
    ECDH_ES_A192KW = -30
    ECDH_ES_A128KW = -29
    ECDH_SS_HKDF_512 = -28
    ECDH_SS_HKDF_256 = -27
    ECDH_ES_HKDF_512 = -26
    ECDH_ES_HKDF_256 = -25
    DIRECT_HKDF_SHA512 = -11
    DIRECT_HKDF_SHA256 = -10
    EDDSA = -8
    ES256 = -7
    DIRECT = -6
    A256KW = -5
    A192KW = -4
    A128KW = -3
    HPKE_V1_BASE = -1
    A128GCM = 1
    A192GCM = 2
    A256GCM = 3
    HS256_64 = 4
    HS256 = 5
    HS384 = 6
    HS512 = 7
    AES_CCM_16_64_128 = 10
    AES_CCM_16_64_256 = 11
    AES_CCM_64_64_128 = 12
    AES_CCM_64_64_256 = 13
    CHACHA20_POLY1305 = 24
    AES_CCM_16_128_128 = 30
    AES_CCM_16_128_256 = 31
    AES_CCM_64_128_128 = 32
    AES_CCM_64_128_256 = 33


class CWTClaims(enum.IntEnum):
    HCERT = -260
    EUPH_NONCE = -259
    EAT_MAROE_PREFIX = -258
    EAT_FDO = -257
    ISS = 1
    SUB = 2
    AUD = 3
    EXP = 4
    NBF = 5
    IAT = 6
    CTI = 7
    CNF = 8
    NONCE = 10
    UEID = 11
    OEMID = 13
    SEC_LEVEL = 14
    SEC_BOOT = 15
    DBG_STAT = 16
    LOCATION = 17
    EAT_PROFILE = 18
    SUBMODS = 20
