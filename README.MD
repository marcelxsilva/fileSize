
Um simples projeto feito para monitorar o tamanho de um determinado arquivo.

Quando o arquivo atingir um determinado tamanho estabelecido é enviado um email informando sobre o tamanho daquele arquivo

Este script foi feito para avaliar o tamanho de um arquivo e enviar um mensagem para o email das pessoas responsaveis informando que tal arquivo 
atingiu o tamanho limite estabelecido, poderia simplifica-lo mais ainda, porem como ele ira rodar em 38 Servidores distintos precisava de uma configuracao rapida e simples, por esse motivo existe o arquivo unityAndFile.txt e email.txt

## Email que enviara para outros emails
No código fonte existe duas variaveis constantes:
#### EMAIL e PASSWORD 
Nelas será definido as informacoes do email que ira enviar os emails


#### unityAndFile.txt
 Dentro do projeto que fiz, existem 38 servidores onde iria rodar este script, então na primeira linha deste arquivo é difinido o nome da unidade
 
 Na segunda linha é definido o local do arquivo a ser avaliado

 #### email.txt
 Deve ser inserido por linha cada email que desejar receber essas mensagens