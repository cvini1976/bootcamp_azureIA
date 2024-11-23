```markdown
# Azure Open AI na VNet - DEV Community

---

**Kenichiro Nakamura**

Postado em: 12 de Outubro de 2023

---

## Azure Open AI na VNet

**#azure #openai #security**

Os modelos GPT estão hospedados em vários fornecedores de serviços no momento, e o Microsoft Azure é um deles. Embora os modelos em si sejam os mesmos, há muitas diferenças, incluindo:

- custo
- funcionalidades
- tipo de modelos e versões
- localização geográfica
- segurança
- suporte
- etc.

Um dos aspectos mais importantes ao usarmos isso em um ambiente empresarial é, claro, a segurança. Ao usar os recursos de segurança de rede do Azure com o Azure Open AI, os clientes podem consumir o serviço Open AI de e dentro da VNet, portanto, nenhuma informação está fluindo em público.

### Implementação de Exemplo

O repositório de amostras do Azure fornece arquivos de bicep de exemplo para implantar o Azure Open AI em um ambiente VNet. GitHub: openai-enterprise-iac. As principais características que o bicep utiliza são:

- Integração VNet
- Ponto de extremidade privado para o Azure Open AI
- Ponto de extremidade privado para a Pesquisa Cognitiva
- Zona DNS privada

Ao usar esses recursos, todo o tráfego de saída do Web App é roteado apenas dentro da VNet e todos os nomes são resolvidos em endereços IP privados. O Open AI e a Pesquisa Cognitiva desativam o endereço IP público, assim, não há mais um endpoint de interface pública disponível.

### Implantar

O arquivo bicep irá implantar os seguintes recursos do Azure.

Vamos implantar e confirmar como funciona. Eu criei um grupo de recursos na região Leste dos EUA para meu próprio teste.

```bash
git clone https://github.com/Azure-Samples/openai-enterprise-iac
cd openai-enterprise-iac
az group create -n openaitest -l eastus
az deployment group create -g openaitest -f .\infra\main.bicep
```

Uma vez que eu execute o comando acima, vejo que a implantação começou. Aguarde até que a implantação seja concluída.

### Teste

Vamos ver se a implantação foi bem-sucedida.

#### Azure Open AI

Vamos tentar o acesso público primeiro. Eu consegui criar uma implantação sem nenhum problema. Mas quando tento pelo playground de Chat no meu Portal do Azure, vejo o seguinte erro.

E quanto ao acesso via API Web? A partir de uma ferramenta avançada do App Service, eu faço login em uma sessão Bash, e primeiro eu faço um ping na URL do serviço.

Eu vejo que o endereço IP privado atribuído ao Ponto de Extremidade Privado está retornando. Então, eu uso o comando curl para enviar uma solicitação ao endpoint.

---

**Comentários Principais** (0)

**Assinar**

---

**Obrigado ao nosso patrocinador Diamante, Neon, por apoiar a nossa comunidade.**

DEV Community — Uma rede social construtiva e inclusiva para desenvolvedores de software. Com você em cada passo da sua jornada.

---

**Início | DEV++ | Podcasts | Vídeos | Tags | Ajuda DEV | Loja Forem | Anuncie no DEV | Desafios DEV | Showcase DEV | Sobre | Contato | Banco de Dados Postgres Gratuito | Guias | Comparações de Software | Código de Conduta | Política de Privacidade | Termos de Uso**

---

Construído em Forem — o software de código aberto que alimenta o DEV e outras comunidades inclusivas. Feito com amor e Ruby on Rails. DEV Community © 2016 - 2024.

---

Nós somos um lugar onde programadores compartilham, ficam atualizados e crescem em suas carreiras.

**Log In | Criar Conta**
```
```markdown
# Azure Open AI na VNet - DEV Community

---

**Kenichiro Nakamura**

Postado em: 12 de Outubro de 2023

---

## Azure Open AI na VNet

**#azure #openai #security**

Os modelos GPT estão hospedados em vários fornecedores de serviços no momento, e o Microsoft Azure é um deles. Embora os modelos em si sejam os mesmos, há muitas diferenças, incluindo:

- custo
- funcionalidades
- tipo de modelos e versões
- localização geográfica
- segurança
- suporte
- etc.

Um dos aspectos mais importantes ao usarmos isso em um ambiente empresarial é, claro, a segurança. Ao usar os recursos de segurança de rede do Azure com o Azure Open AI, os clientes podem consumir o serviço Open AI de e dentro da VNet, portanto, nenhuma informação está fluindo em público.

### Implementação de Exemplo

O repositório de amostras do Azure fornece arquivos de bicep de exemplo para implantar o Azure Open AI em um ambiente VNet. GitHub: openai-enterprise-iac. As principais características que o bicep utiliza são:

- Integração VNet
- Ponto de extremidade privado para o Azure Open AI
- Ponto de extremidade privado para a Pesquisa Cognitiva
- Zona DNS privada

Ao usar esses recursos, todo o tráfego de saída do Web App é roteado apenas dentro da VNet e todos os nomes são resolvidos em endereços IP privados. O Open AI e a Pesquisa Cognitiva desativam o endereço IP público, assim, não há mais um endpoint de interface pública disponível.

### Implantar

O arquivo bicep irá implantar os seguintes recursos do Azure.

Vamos implantar e confirmar como funciona. Eu criei um grupo de recursos na região Leste dos EUA para meu próprio teste.

```bash
git clone https://github.com/Azure-Samples/openai-enterprise-iac
cd openai-enterprise-iac
az group create -n openaitest -l eastus
az deployment group create -g openaitest -f .\infra\main.bicep
```

Uma vez que eu execute o comando acima, vejo que a implantação começou. Aguarde até que a implantação seja concluída.

### Teste

Vamos ver se a implantação foi bem-sucedida.

#### Azure Open AI

Vamos tentar o acesso público primeiro. Eu consegui criar uma implantação sem nenhum problema. Mas quando tento pelo playground de Chat no meu Portal do Azure, vejo o seguinte erro.

E quanto ao acesso via API Web? A partir de uma ferramenta avançada do App Service, eu faço login em uma sessão Bash, e primeiro eu faço um ping na URL do serviço.

Eu vejo que o endereço IP privado atribuído ao Ponto de Extremidade Privado está retornando. Então, eu uso o comando curl para enviar uma solicitação ao endpoint.

---

**Comentários Principais** (0)

**Assinar**

---

**Obrigado ao nosso patrocinador Diamante, Neon, por apoiar a nossa comunidade.**

DEV Community — Uma rede social construtiva e inclusiva para desenvolvedores de software. Com você em cada passo da sua jornada.

---

**Início | DEV++ | Podcasts | Vídeos | Tags | Ajuda DEV | Loja Forem | Anuncie no DEV | Desafios DEV | Showcase DEV | Sobre | Contato | Banco de Dados Postgres Gratuito | Guias | Comparações de Software | Código de Conduta | Política de Privacidade | Termos de Uso**

---

Construído em Forem — o software de código aberto que alimenta o DEV e outras comunidades inclusivas. Feito com amor e Ruby on Rails. DEV Community © 2016 - 2024.

---

Nós somos um lugar onde programadores compartilham, ficam atualizados e crescem em suas carreiras.

**Log In | Criar Conta**