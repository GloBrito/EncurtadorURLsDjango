# Encurteco
O **encur**tador de URLs dos Buser**teco**s
<br>
https://encurteco.herokuapp.com/

Projeto colaborativo de encurtador de URLs/links utilizando PostgreSQL, Python e o framework Django.
<br>
Deploy feito na plataforma HerokuApp (disponível até 28 de novembro de 2022).

### Página inicial
![encurteco-home](https://user-images.githubusercontent.com/77248375/195873629-c2c6f0cc-16eb-4928-8fe5-94da3a1cce68.png)
O usuário é instruído a indicar a URL que deseja encurtar e a escrever uma expressão curta que irá personalização a URL.

### Página de sucesso
![encurteco-sucesso](https://user-images.githubusercontent.com/77248375/195874274-9eb1f8c6-6b40-4bd4-8c94-54db876c19b0.png)
Caso a personalização ainda não exista no banco de dados o link será encurtado com sucesso e mostrado nessa nova página.
<br>
O usuário poderá copiar a URL criada para a área de transferência clicando no botão ao lado do link criado.

### Página de link já existente
![encurteco-existente](https://user-images.githubusercontent.com/77248375/195874311-206e9ba5-ddcc-4e20-8523-13e7715c1519.png)
Cada link personalizado é único, por isso se o usuário tentar inserir uma personalização que já existe será levado a essa página.

### Página não encontrada
![encurteco-404](https://user-images.githubusercontent.com/77248375/195874298-51f5b654-680e-4591-8f08-f56e18bb0782.png)
Em caso de tentar acessar um link encurtado que não existe cairá nessa página de erro.

## Feito por:
<a href = "https://github.com/andradebru">
  <img src = "https://avatars.githubusercontent.com/u/77248375?v=4" style="width: 100px; border-radius:50%; /">
</a>
<a href = "https://github.com/evandropcs" text-decoration: none;">
  <img src = "https://avatars.githubusercontent.com/u/75592344?v=4" style="width:100px;"/>
</a>
<a href = "https://github.com/GloBrito/" style="text-decoration: none;">
  <img src = "https://avatars.githubusercontent.com/u/103264347?v=4" style="width:100px;"/>
</a>

Feito com ♥ durante o programa de estágio Buser Tech.

