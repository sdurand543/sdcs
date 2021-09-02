#!/bin/bash

reset () {
    python $SCRITER_SRC_PATH/scriter.py reset
}

use () {
    python $SCRITER_SRC_PATH/scriter.py use $1
}

iter () {
    python $SCRITER_SRC_PATH/scriter.py iter
}

info () {
    python $SCRITER_SRC_PATH/scriter.py info
}

next () {
    python $SCRITER_SRC_PATH/scriter.py next
}

export SCRITER_SRC_PATH=$PWD
python $SCRITER_SRC_PATH/scriter.py init_persistence
