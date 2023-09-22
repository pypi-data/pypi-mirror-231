#!/usr/bin/env bash

DIR_TARGET="crumbcutter"

# Search for the target directory upwards
search_for_directory() {
    local target_dir="$1"
    local max_attempts="$2"
    local current_dir="$PWD"
    local attempts=0
    local last_found_dir=""

    while [[ $attempts -lt $max_attempts ]]; do
        if [[ -d "$current_dir/$target_dir" ]]; then
            last_found_dir="$current_dir/$target_dir"
        fi

        # Move up one directory
        current_dir=$(dirname "$current_dir")
        ((attempts++))
    done

    if [[ -n "$last_found_dir" ]]; then
        echo "Using $target_dir at $last_found_dir"
        cd "$last_found_dir" || exit
        return 0
    else
        echo "$target_dir not found after $max_attempts attempts."
        return 1
    fi
}

# Search for the directory and change to it if found
search_for_directory "$DIR_TARGET" 10

# Check if act is installed
if ! [ -f ./bin/act ]; then
    echo "act not found, downloading and installing..."
    # Download and install act
    curl https://raw.githubusercontent.com/nektos/act/master/install.sh | bash
else
    echo "act is already installed"
fi

# Create .actrc file with default configuration
echo "-P ubuntu-18.04=nektos/act-environments-ubuntu:18.04" >.actrc

# Execute act
./bin/act 2>&1 | tee log.txt
