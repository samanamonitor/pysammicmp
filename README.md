# Build package
`docker run -it --rm -v $(pwd):/usr/src samm-repo /usr/local/bin/build-deb.sh`
# Add to repo
`docker run --rm -it -v $(pwd):/usr/src -w /usr/src samm-repo /usr/local/bin/add-file-repo.sh <package>  jammy amd64`
