$service = $Args[0]
if (!$service) {
    docker-compose -p 'study-one' -f ./docker-compose.yml build --parallel --force-rm
}else {
    docker-compose -p 'study-one' -f ./docker-compose.yml build  $service
}
./up.ps1