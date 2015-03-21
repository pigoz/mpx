#include "bridge.h"
#include <stdio.h>

void ctest() {
    mpv_handle *mpv = mpv_create();
    printf("Hello World from C!\n");
    mpv_detach_destroy(mpv);
}
