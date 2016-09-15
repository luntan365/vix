
class VixError(Exception):
    ERRORS = {
        0: 'VIX_OK',

        # General errors
        1: 'VIX_E_FAIL',
        2: 'VIX_E_OUT_OF_MEMORY',
        3: 'VIX_E_INVALID_ARG',
        4: 'VIX_E_FILE_NOT_FOUND',
        5: 'VIX_E_OBJECT_IS_BUSY',
        6: 'VIX_E_NOT_SUPPORTED',
        7: 'VIX_E_FILE_ERROR',
        8: 'VIX_E_DISK_FULL',
        9: 'VIX_E_INCORRECT_FILE_TYPE',
        10: 'VIX_E_CANCELLED',
        11: 'VIX_E_FILE_READ_ONLY',
        12: 'VIX_E_FILE_ALREADY_EXISTS',
        13: 'VIX_E_FILE_ACCESS_ERROR',
        14: 'VIX_E_REQUIRES_LARGE_FILES',
        15: 'VIX_E_FILE_ALREADY_LOCKED',
        16: 'VIX_E_VMDB',
        20: 'VIX_E_NOT_SUPPORTED_ON_REMOTE_OBJECT',
        21: 'VIX_E_FILE_TOO_BIG',
        22: 'VIX_E_FILE_NAME_INVALID',
        23: 'VIX_E_ALREADY_EXISTS',
        24: 'VIX_E_BUFFER_TOOSMALL',
        25: 'VIX_E_OBJECT_NOT_FOUND',
        26: 'VIX_E_HOST_NOT_CONNECTED',
        27: 'VIX_E_INVALID_UTF8_STRING',
        31: 'VIX_E_OPERATION_ALREADY_IN_PROGRESS',
        29: 'VIX_E_UNFINISHED_JOB',
        30: 'VIX_E_NEED_KEY',
        32: 'VIX_E_LICENSE',
        34: 'VIX_E_VM_HOST_DISCONNECTED',
        35: 'VIX_E_AUTHENTICATION_FAIL',
        36: 'VIX_E_HOST_CONNECTION_LOST',
        41: 'VIX_E_DUPLICATE_NAME',
        44: 'VIX_E_ARGUMENT_TOO_BIG',

        # Handle Errors
        1000: 'VIX_E_INVALID_HANDLE',
        1001: 'VIX_E_NOT_SUPPORTED_ON_HANDLE_TYPE',
        1002: 'VIX_E_TOO_MANY_HANDLES',

        # XML errors
        2000: 'VIX_E_NOT_FOUND',
        2001: 'VIX_E_TYPE_MISMATCH',
        2002: 'VIX_E_INVALID_XML',

        # VM Control Errors
        3000: 'VIX_E_TIMEOUT_WAITING_FOR_TOOLS',
        3001: 'VIX_E_UNRECOGNIZED_COMMAND',
        3003: 'VIX_E_OP_NOT_SUPPORTED_ON_GUEST',
        3004: 'VIX_E_PROGRAM_NOT_STARTED',
        3005: 'VIX_E_CANNOT_START_READ_ONLY_VM',
        3006: 'VIX_E_VM_NOT_RUNNING',
        3007: 'VIX_E_VM_IS_RUNNING',
        3008: 'VIX_E_CANNOT_CONNECT_TO_VM',
        3009: 'VIX_E_POWEROP_SCRIPTS_NOT_AVAILABLE',
        3010: 'VIX_E_NO_GUEST_OS_INSTALLED',
        3011: 'VIX_E_VM_INSUFFICIENT_HOST_MEMORY',
        3012: 'VIX_E_SUSPEND_ERROR',
        3013: 'VIX_E_VM_NOT_ENOUGH_CPUS',
        3014: 'VIX_E_HOST_USER_PERMISSIONS',
        3015: 'VIX_E_GUEST_USER_PERMISSIONS',
        3016: 'VIX_E_TOOLS_NOT_RUNNING',
        3017: 'VIX_E_GUEST_OPERATIONS_PROHIBITED',
        3018: 'VIX_E_ANON_GUEST_OPERATIONS_PROHIBITED',
        3019: 'VIX_E_ROOT_GUEST_OPERATIONS_PROHIBITED',
        3023: 'VIX_E_MISSING_ANON_GUEST_ACCOUNT',
        3024: 'VIX_E_CANNOT_AUTHENTICATE_WITH_GUEST',
        3025: 'VIX_E_UNRECOGNIZED_COMMAND_IN_GUEST',
        3026: 'VIX_E_CONSOLE_GUEST_OPERATIONS_PROHIBITED',
        3027: 'VIX_E_MUST_BE_CONSOLE_USER',
        3028: 'VIX_E_VMX_MSG_DIALOG_AND_NO_UI',
        3031: 'VIX_E_OPERATION_NOT_ALLOWED_FOR_LOGIN_TYPE',
        3032: 'VIX_E_LOGIN_TYPE_NOT_SUPPORTED',
        3033: 'VIX_E_EMPTY_PASSWORD_NOT_ALLOWED_IN_GUEST',
        3034: 'VIX_E_INTERACTIVE_SESSION_NOT_PRESENT',
        3035: 'VIX_E_INTERACTIVE_SESSION_USER_MISMATCH',
        3041: 'VIX_E_CANNOT_POWER_ON_VM',
        3043: 'VIX_E_NO_DISPLAY_SERVER',
        3046: 'VIX_E_TOO_MANY_LOGONS',
        3047: 'VIX_E_INVALID_AUTHENTICATION_SESSION',

        # VM Errors
        4000: 'VIX_E_VM_NOT_FOUND',
        4001: 'VIX_E_NOT_SUPPORTED_FOR_VM_VERSION',
        4002: 'VIX_E_CANNOT_READ_VM_CONFIG',
        4003: 'VIX_E_TEMPLATE_VM',
        4004: 'VIX_E_VM_ALREADY_LOADED',
        4006: 'VIX_E_VM_ALREADY_UP_TO_DATE',
        4011: 'VIX_E_VM_UNSUPPORTED_GUEST',

        # Property Errors
        6000: 'VIX_E_UNRECOGNIZED_PROPERTY',
        6001: 'VIX_E_INVALID_PROPERTY_VALUE',
        6002: 'VIX_E_READ_ONLY_PROPERTY',
        6003: 'VIX_E_MISSING_REQUIRED_PROPERTY',
        6004: 'VIX_E_INVALID_SERIALIZED_DATA',
        6005: 'VIX_E_PROPERTY_TYPE_MISMATCH',

        # Completion Errors
        8000: 'VIX_E_BAD_VM_INDEX',

        # Message errors
        10000: 'VIX_E_INVALID_MESSAGE_HEADER',
        10001: 'VIX_E_INVALID_MESSAGE_BODY',

        # Snapshot errors
        13000: 'VIX_E_SNAPSHOT_INVAL',
        13001: 'VIX_E_SNAPSHOT_DUMPER',
        13002: 'VIX_E_SNAPSHOT_DISKLIB',
        13003: 'VIX_E_SNAPSHOT_NOTFOUND',
        13004: 'VIX_E_SNAPSHOT_EXISTS',
        13005: 'VIX_E_SNAPSHOT_VERSION',
        13006: 'VIX_E_SNAPSHOT_NOPERM',
        13007: 'VIX_E_SNAPSHOT_CONFIG',
        13008: 'VIX_E_SNAPSHOT_NOCHANGE',
        13009: 'VIX_E_SNAPSHOT_CHECKPOINT',
        13010: 'VIX_E_SNAPSHOT_LOCKED',
        13011: 'VIX_E_SNAPSHOT_INCONSISTENT',
        13012: 'VIX_E_SNAPSHOT_NAMETOOLONG',
        13013: 'VIX_E_SNAPSHOT_VIXFILE',
        13014: 'VIX_E_SNAPSHOT_DISKLOCKED',
        13015: 'VIX_E_SNAPSHOT_DUPLICATEDDISK',
        13016: 'VIX_E_SNAPSHOT_INDEPENDENTDISK',
        13017: 'VIX_E_SNAPSHOT_NONUNIQUE_NAME',
        13018: 'VIX_E_SNAPSHOT_MEMORY_ON_INDEPENDENT_DISK',
        13019: 'VIX_E_SNAPSHOT_MAXSNAPSHOTS',
        13020: 'VIX_E_SNAPSHOT_MIN_FREE_SPACE',
        13021: 'VIX_E_SNAPSHOT_HIERARCHY_TOODEEP',
        13024: 'VIX_E_SNAPSHOT_NOT_REVERTABLE',

        # Host Errors
        14003: 'VIX_E_HOST_DISK_INVALID_VALUE',
        14004: 'VIX_E_HOST_DISK_SECTORSIZE',
        14005: 'VIX_E_HOST_FILE_ERROR_EOF',
        14006: 'VIX_E_HOST_NETBLKDEV_HANDSHAKE',
        14007: 'VIX_E_HOST_SOCKET_CREATION_ERROR',
        14008: 'VIX_E_HOST_SERVER_NOT_FOUND',
        14009: 'VIX_E_HOST_NETWORK_CONN_REFUSED',
        14010: 'VIX_E_HOST_TCP_SOCKET_ERROR',
        14011: 'VIX_E_HOST_TCP_CONN_LOST',
        14012: 'VIX_E_HOST_NBD_HASHFILE_VOLUME',
        14013: 'VIX_E_HOST_NBD_HASHFILE_INIT',

        # Disklib errors
        16000: 'VIX_E_DISK_INVAL',
        16001: 'VIX_E_DISK_NOINIT',
        16002: 'VIX_E_DISK_NOIO',
        16003: 'VIX_E_DISK_PARTIALCHAIN',
        16006: 'VIX_E_DISK_NEEDSREPAIR',
        16007: 'VIX_E_DISK_OUTOFRANGE',
        16008: 'VIX_E_DISK_CID_MISMATCH',
        16009: 'VIX_E_DISK_CANTSHRINK',
        16010: 'VIX_E_DISK_PARTMISMATCH',
        16011: 'VIX_E_DISK_UNSUPPORTEDDISKVERSION',
        16012: 'VIX_E_DISK_OPENPARENT',
        16013: 'VIX_E_DISK_NOTSUPPORTED',
        16014: 'VIX_E_DISK_NEEDKEY',
        16015: 'VIX_E_DISK_NOKEYOVERRIDE',
        16016: 'VIX_E_DISK_NOTENCRYPTED',
        16017: 'VIX_E_DISK_NOKEY',
        16018: 'VIX_E_DISK_INVALIDPARTITIONTABLE',
        16019: 'VIX_E_DISK_NOTNORMAL',
        16020: 'VIX_E_DISK_NOTENCDESC',
        16022: 'VIX_E_DISK_NEEDVMFS',
        16024: 'VIX_E_DISK_RAWTOOBIG',
        16027: 'VIX_E_DISK_TOOMANYOPENFILES',
        16028: 'VIX_E_DISK_TOOMANYREDO',
        16029: 'VIX_E_DISK_RAWTOOSMALL',
        16030: 'VIX_E_DISK_INVALIDCHAIN',
        16052: 'VIX_E_DISK_KEY_NOTFOUND',
        16053: 'VIX_E_DISK_SUBSYSTEM_INIT_FAIL',
        16054: 'VIX_E_DISK_INVALID_CONNECTION',
        16061: 'VIX_E_DISK_ENCODING',
        16062: 'VIX_E_DISK_CANTREPAIR',
        16063: 'VIX_E_DISK_INVALIDDISK',
        16064: 'VIX_E_DISK_NOLICENSE',
        16065: 'VIX_E_DISK_NODEVICE',
        16066: 'VIX_E_DISK_UNSUPPORTEDDEVICE',
        16067: 'VIX_E_DISK_CAPACITY_MISMATCH',
        16068: 'VIX_E_DISK_PARENT_NOTALLOWED',
        16069: 'VIX_E_DISK_ATTACH_ROOTLINK',

        # Crypto Library Errors
        17000: 'VIX_E_CRYPTO_UNKNOWN_ALGORITHM',
        17001: 'VIX_E_CRYPTO_BAD_BUFFER_SIZE',
        17002: 'VIX_E_CRYPTO_INVALID_OPERATION',
        17003: 'VIX_E_CRYPTO_RANDOM_DEVICE',
        17004: 'VIX_E_CRYPTO_NEED_PASSWORD',
        17005: 'VIX_E_CRYPTO_BAD_PASSWORD',
        17006: 'VIX_E_CRYPTO_NOT_IN_DICTIONARY',
        17007: 'VIX_E_CRYPTO_NO_CRYPTO',
        17008: 'VIX_E_CRYPTO_ERROR',
        17009: 'VIX_E_CRYPTO_BAD_FORMAT',
        17010: 'VIX_E_CRYPTO_LOCKED',
        17011: 'VIX_E_CRYPTO_EMPTY',
        17012: 'VIX_E_CRYPTO_KEYSAFE_LOCATOR',

        # Remoting Errors.
        18000: 'VIX_E_CANNOT_CONNECT_TO_HOST',
        18001: 'VIX_E_NOT_FOR_REMOTE_HOST',
        18002: 'VIX_E_INVALID_HOSTNAME_SPECIFICATION',

        # Screen Capture Errors.
        19000: 'VIX_E_SCREEN_CAPTURE_ERROR',
        19001: 'VIX_E_SCREEN_CAPTURE_BAD_FORMAT',
        19002: 'VIX_E_SCREEN_CAPTURE_COMPRESSION_FAIL',
        19003: 'VIX_E_SCREEN_CAPTURE_LARGE_DATA',

        # Guest Errors
        20000: 'VIX_E_GUEST_VOLUMES_NOT_FROZEN',
        20001: 'VIX_E_NOT_A_FILE',
        20002: 'VIX_E_NOT_A_DIRECTORY',
        20003: 'VIX_E_NO_SUCH_PROCESS',
        20004: 'VIX_E_FILE_NAME_TOO_LONG',
        20005: 'VIX_E_OPERATION_DISABLED',

        # Tools install errors
        21000: 'VIX_E_TOOLS_INSTALL_NO_IMAGE',
        21001: 'VIX_E_TOOLS_INSTALL_IMAGE_INACCESIBLE',
        21002: 'VIX_E_TOOLS_INSTALL_NO_DEVICE',
        21003: 'VIX_E_TOOLS_INSTALL_DEVICE_NOT_CONNECTED',
        21004: 'VIX_E_TOOLS_INSTALL_CANCELLED',
        21005: 'VIX_E_TOOLS_INSTALL_INIT_FAILED',
        21006: 'VIX_E_TOOLS_INSTALL_AUTO_NOT_SUPPORTED',
        21007: 'VIX_E_TOOLS_INSTALL_GUEST_NOT_READY',
        21009: 'VIX_E_TOOLS_INSTALL_ERROR',
        21010: 'VIX_E_TOOLS_INSTALL_ALREADY_UP_TO_DATE',
        21011: 'VIX_E_TOOLS_INSTALL_IN_PROGRESS',
        21012: 'VIX_E_TOOLS_INSTALL_IMAGE_COPY_FAILED',

        # Wrapper Errors
        22001: 'VIX_E_WRAPPER_WORKSTATION_NOT_INSTALLED',
        22002: 'VIX_E_WRAPPER_VERSION_NOT_FOUND',
        22003: 'VIX_E_WRAPPER_SERVICEPROVIDER_NOT_FOUND',
        22004: 'VIX_E_WRAPPER_PLAYER_NOT_INSTALLED',
        22005: 'VIX_E_WRAPPER_RUNTIME_NOT_INSTALLED',
        22006: 'VIX_E_WRAPPER_MULTIPLE_SERVICEPROVIDERS',

        # FuseMnt errors
        24000: 'VIX_E_MNTAPI_MOUNTPT_NOT_FOUND',
        24001: 'VIX_E_MNTAPI_MOUNTPT_IN_USE',
        24002: 'VIX_E_MNTAPI_DISK_NOT_FOUND',
        24003: 'VIX_E_MNTAPI_DISK_NOT_MOUNTED',
        24004: 'VIX_E_MNTAPI_DISK_IS_MOUNTED',
        24005: 'VIX_E_MNTAPI_DISK_NOT_SAFE',
        24006: 'VIX_E_MNTAPI_DISK_CANT_OPEN',
        24007: 'VIX_E_MNTAPI_CANT_READ_PARTS',
        24008: 'VIX_E_MNTAPI_UMOUNT_APP_NOT_FOUND',
        24009: 'VIX_E_MNTAPI_UMOUNT',
        24010: 'VIX_E_MNTAPI_NO_MOUNTABLE_PARTITONS',
        24011: 'VIX_E_MNTAPI_PARTITION_RANGE',
        24012: 'VIX_E_MNTAPI_PERM',
        24013: 'VIX_E_MNTAPI_DICT',
        24014: 'VIX_E_MNTAPI_DICT_LOCKED',
        24015: 'VIX_E_MNTAPI_OPEN_HANDLES',
        24016: 'VIX_E_MNTAPI_CANT_MAKE_VAR_DIR',
        24017: 'VIX_E_MNTAPI_NO_ROOT',
        24018: 'VIX_E_MNTAPI_LOOP_FAILED',
        24019: 'VIX_E_MNTAPI_DAEMON',
        24020: 'VIX_E_MNTAPI_INTERNAL',
        24021: 'VIX_E_MNTAPI_SYSTEM',
        24022: 'VIX_E_MNTAPI_NO_CONNECTION_DETAILS',

        # VixMntapi errors
        24300: 'VIX_E_MNTAPI_INCOMPATIBLE_VERSION',
        24301: 'VIX_E_MNTAPI_OS_ERROR',
        24302: 'VIX_E_MNTAPI_DRIVE_LETTER_IN_USE',
        24303: 'VIX_E_MNTAPI_DRIVE_LETTER_ALREADY_ASSIGNED',
        24304: 'VIX_E_MNTAPI_VOLUME_NOT_MOUNTED',
        24305: 'VIX_E_MNTAPI_VOLUME_ALREADY_MOUNTED',
        24306: 'VIX_E_MNTAPI_FORMAT_FAILURE',
        24307: 'VIX_E_MNTAPI_NO_DRIVER',
        24308: 'VIX_E_MNTAPI_ALREADY_OPENED',
        24309: 'VIX_E_MNTAPI_ITEM_NOT_FOUND',
        24310: 'VIX_E_MNTAPI_UNSUPPROTED_BOOT_LOADER',
        24311: 'VIX_E_MNTAPI_UNSUPPROTED_OS',
        24312: 'VIX_E_MNTAPI_CODECONVERSION',
        24313: 'VIX_E_MNTAPI_REGWRITE_ERROR',
        24314: 'VIX_E_MNTAPI_UNSUPPORTED_FT_VOLUME',
        24315: 'VIX_E_MNTAPI_PARTITION_NOT_FOUND',
        24316: 'VIX_E_MNTAPI_PUTFILE_ERROR',
        24317: 'VIX_E_MNTAPI_GETFILE_ERROR',
        24318: 'VIX_E_MNTAPI_REG_NOT_OPENED',
        24319: 'VIX_E_MNTAPI_REGDELKEY_ERROR',
        24320: 'VIX_E_MNTAPI_CREATE_PARTITIONTABLE_ERROR',
        24321: 'VIX_E_MNTAPI_OPEN_FAILURE',
        24322: 'VIX_E_MNTAPI_VOLUME_NOT_WRITABLE',

        # Success on operation that completes asynchronously
        25000: 'VIX_ASYNC',

        # Async errors
        26000: 'VIX_E_ASYNC_MIXEDMODE_UNSUPPORTED',

        # Network Errors
        30001: 'VIX_E_NET_HTTP_UNSUPPORTED_PROTOCOL',
        30003: 'VIX_E_NET_HTTP_URL_MALFORMAT',
        30005: 'VIX_E_NET_HTTP_COULDNT_RESOLVE_PROXY',
        30006: 'VIX_E_NET_HTTP_COULDNT_RESOLVE_HOST',
        30007: 'VIX_E_NET_HTTP_COULDNT_CONNECT',
        30022: 'VIX_E_NET_HTTP_HTTP_RETURNED_ERROR',
        30028: 'VIX_E_NET_HTTP_OPERATION_TIMEDOUT',
        30035: 'VIX_E_NET_HTTP_SSL_CONNECT_ERROR',
        30047: 'VIX_E_NET_HTTP_TOO_MANY_REDIRECTS',
        30200: 'VIX_E_NET_HTTP_TRANSFER',
        30201: 'VIX_E_NET_HTTP_SSL_SECURITY',
        30202: 'VIX_E_NET_HTTP_GENERIC',
    }

    def __init__(self, error_code):
        self._error = error_code

    def __str__(self):
        return "<VixError {1} ({0})>".format(str(self._error), self.ERRORS.get(self._error) or "?")

for error_code in VixError.ERRORS:
    setattr(VixError, VixError.ERRORS[error_code], error_code)