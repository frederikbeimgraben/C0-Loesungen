
# more shell commands for Informatik 2 to mange the docker-image version
version_c0() { docker images --format="{{.Repository}} {{.ID}}" | grep "^dbatunituebingen/c0" | cut -d' ' -f2 | head -n1; }
update_c0() { (version_c0 | xargs docker rmi) 2>/dev/null; docker pull dbatunituebingen/c0:latest; }
