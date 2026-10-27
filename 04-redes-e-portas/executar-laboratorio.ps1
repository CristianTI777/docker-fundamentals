Write-Host "=== 1. Criando e inspecionando rede customizada ===" -ForegroundColor Cyan
docker network create minha-primeira-rede
docker network ls

Write-Host "`n=== 2. Testando isolamento e conexao dinamica ===" -ForegroundColor Cyan
docker run -d --name app --network minha-primeira-rede nginx
docker run -d --name app2 nginx
docker network connect minha-primeira-rede app2
docker inspect app2 --format '{{json .NetworkSettings.Networks}}'

Write-Host "`n=== 3. Testando Mapeamento com Binding Seguro (127.0.0.1) ===" -ForegroundColor Cyan
docker rm -f app app2
docker run -d --name app-seguro -p 127.0.0.1:8080:80 nginx
curl.exe http://localhost:8080

Write-Host "`n=== 4. Testando Publicacao Dinamica (-P) ===" -ForegroundColor Cyan
docker run -d --name app-dinamico -P nginx
docker ps --filter "name=app-dinamico"

Write-Host "`n=== 5. Limpeza de Recursos ===" -ForegroundColor Yellow
docker rm -f app-seguro app-dinamico
docker network rm minha-primeira-rede
Write-Host "Laboratório finalizado e recursos liberados!" -ForegroundColor Green