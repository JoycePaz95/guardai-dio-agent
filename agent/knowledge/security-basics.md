# Base de Conhecimento: GuardAI Security Framework

## 1. Pilares da Análise de Segurança
* **Ativo:** Qualquer recurso de valor para a operação (banco de dados, código-fonte, credenciais, servidor).
* **Vulnerabilidade:** Brecha técnica, lógica ou de configuração que expõe um ativo.
* **Ameaça:** Vetor ou agente capaz de explorar uma brecha (ex.: atacante externo, script automatizado, erro interno).
* **Risco:** Cenário resultante do cruzamento entre a **probabilidade** de exploração e o **impacto** no negócio.

## 2. Tríade CID + Autenticidade
* **Confidencialidade:** Controle rigoroso de acesso e criptografia em trânsito (TLS) e em repouso.
* **Integridade:** Garantia de que dados e códigos não sofreram adulteração não autorizada (hashes, assinaturas, validação).
* **Disponibilidade:** Resiliência contra quedas, sobrecarga (DoS) e falhas operacionais.
* **Autenticidade & Não Repúdio:** Certeza sobre a identidade de quem executa cada ação e registro auditável (logs).

## 3. Matriz Rápida de Severidade
* **Crítica:** Exploração trivial e impacto total (ex.: RCE, SQL Injection sem autenticação, credenciais expostas).
* **Alta:** Exige alguma condição prévia, mas compromete dados sensíveis ou privilégios administrativos.
* **Média:** Impacto limitado ou exige interação complexa do usuário (ex.: XSS refletido sem acesso a sessão crítica).
* **Baixa:** Falhas informativas ou de configuração com risco residual mínimo.

## 4. Princípios Defensivos Inegociáveis
* **Zero Trust (Confiança Zero):** Validar toda requisição, independentemente da origem na rede.
* **Menor Privilégio:** Contas de serviço, bancos de dados e usuários devem operar com a permissão mínima necessária.
* **Sanitização e Parametrização:** Tratar toda entrada externa como hostil; nunca concatenar strings em queries ou comandos de sistema.
* **Segurança por Padrão (Secure by Default):** Serviços expostos devem iniciar com portas fechadas, firewall ativo e autenticação forte.

