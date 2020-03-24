# Desafio Backend tembici.

Pense nisso como um projeto de código aberto. Deixa de uma forma que você ficasse impressionado se visse isto no Github.
Como isso ficaria, para que você ficasse impressionado se o encontrasse no Github? Agora vá fazer isso.

Tente limitar a quantidade de tempo gasto nisso para no máximo 4 horas. No entanto, sinta-se à vontade para gastar mais - apenas verifique se você está satisfeito com seu envio!

_Dica_: Estamos procurando um envio de alta qualidade, não uma abordagem do tipo "apenas faça-o". Lembre-se de que este teste é a sua oportunidade de nos mostrar como você pensa; portanto, seja claro sobre como você está pensando em seu código - seja com comentários, testes, como você nomeia coisas etc. Você será avaliado tanto pelas funcionalidade do seu código quanto pela utilização de boas práticas, desenvolva como se fosse um código de produção em um time e não uma prova ou script.

## Forma de entrega
Fazer um fork deste projeto e nos enviar a url do seu fork.

## O que fazer

### Primeiro

Crie uma nova aplicação em Python (qualquer framework está valendo, preferimos o Django)


### Descrição da Tarefa

Queremos mostrar no nosso aplicativo as últimas viagens do usuário logado. Também queremos que o nosso usuário possa classificar e dar uma nota para cada viagem.
Sabendo disto o nosso pessoal de mobile precisa de uma API no backend para que possa colocar estas funcionalidades no nosso aplicativo.

Nesta API precisamos:
- Antenticação de usuário no padrão JWT (Não precisa dos endpoints para criar o usuário, mas somente o endpoint que recebe o email e senha do usuário e já faça a sua autenticação na API)
- Endpoint para listar as últimas viagens do usuário logado
- Endpoint para enviar a classificação da viagem e a sua nota

### Payload dos objetos

#### Viagem

```json
{
  "id": 123,
  "data_inicio": "2020-02-20T12:10:00Z",
  "data_fim": "2020-02-20T12:20:00Z",
  "classificacao": 1,
  "nota": 3
}
```

_Obs_: A nota da viagem varia de 1 à 5

#### Classificação da Viagem

```json
[
{
  "id": 1,
  "classificacao": "Trabalho"
},
{
  "id": 2,
  "classificacao": "Atividade física"
},
{
  "id": 3,
  "classificacao": "Lazer"
},
{
  "id": 4,
  "classificacao": "Deslocamento"
}
]
```

### Banco de dados

Você pode usar o SQLite para persistir os dados da nossa aplicação.

**Boa sorte!**
