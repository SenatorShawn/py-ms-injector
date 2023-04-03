from __future__ import annotations

from time import sleep

import pymem
import pymem.process
from pydantic import validate_arguments
from pymem.exception import CouldNotOpenProcess, ProcessNotFound


@validate_arguments
def bypass_ngs(*, sleep_time: int | float = 10.0):
    proc = pymem.Pymem()
    print("Looking for `BlackCipher64.aes`...")
    while True:
        try:
            proc.open_process_from_name("BlackCipher64.aes")
        except (TypeError, ProcessNotFound, CouldNotOpenProcess):
            pass
        else:
            print("Attached to `BlackCipher64.aes`!")
            sleep_time = float(sleep_time)
            # Ensure that we wait long enough to avoid crashing the process...
            sleep(10.)
            break

    base = proc.base_address
    # Second item on the stack trace when breaking at KERNEL32.module32nextw
    offset = 0x2842fc2
    inject = base + offset

    print(f"Writing bypass to BlackCipher64.aes+{offset:02x} ({inject:02x})")
    # Sleep the thread indefinitely at the inject address.
    # # MOV rcx,0xFFFFFFFF
    # # CALL KERNEL32.Sleep
    byte_str = (
        b"\x48\xb9\xff\xff\xff\xff\x00\x00\x00\x00"
        b"\xff\x15\x02\x00\x00\x00\xeb\x08\x70\xb5\x8c\xc1\xfc\x7f\x00"
    )
    proc.write_bytes(inject, byte_str, len(byte_str))
    print("Bypass successfully written.")


if __name__ == "__main__":
    bypass_ngs()
