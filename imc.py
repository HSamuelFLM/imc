# app.py
# ============================================================================
# CALCULADORA DE IMC - VERSÃO BACKEND 
# ============================================================================

# Importa o módulo sys para ter acesso a funcionalidades do sistema
# como por exemplo, encerrar o programa
import sys

# ============================================================================
# FUNÇÃO PARA CALCULAR O IMC
# ============================================================================

def calcular_imc(peso, altura):
    """
    Função que recebe peso (kg) e altura (m) e retorna o IMC calculado
    
    Args:
        peso (float): peso em quilogramas
        altura (float): altura em metros
    
    Returns:
        float: valor do IMC calculado
    """
    # Fórmula do IMC: peso dividido pela altura ao quadrado
    # ** é o operador de exponenciação em Python
    imc = peso / (altura ** 2)
    
    # Retorna o valor do IMC
    return imc


# ============================================================================
# FUNÇÃO PARA CLASSIFICAR O IMC
# ============================================================================

def classificar_imc(imc):
    """
    Função que recebe o valor do IMC e retorna a classificação correspondente
    de acordo com a tabela da Organização Mundial da Saúde (OMS)
    
    Args:
        imc (float): valor do IMC calculado
    
    Returns:
        str: classificação do IMC
    """
    
    # Estrutura condicional if/elif/else para verificar em qual faixa o IMC se encaixa
    # A ordem é importante: da condição mais restritiva para a menos restritiva
    
    # Verifica se o IMC é menor que 18.5
    if imc < 18.5:
        # Se for verdadeiro, retorna "Abaixo do peso"
        return "Abaixo do peso"
    
    # Verifica se o IMC está entre 18.5 e 24.99
    # (não precisa verificar o limite inferior porque o if anterior já excluiu valores < 18.5)
    elif imc < 25:
        return "Peso normal"
    
    # Verifica se o IMC está entre 25 e 29.99
    elif imc < 30:
        return "Sobrepeso"
    
    # Verifica se o IMC está entre 30 e 34.99
    elif imc < 35:
        return "Obesidade grau I"
    
    # Verifica se o IMC está entre 35 e 39.99
    elif imc < 40:
        return "Obesidade grau II"
    
    # Se nenhuma das condições anteriores for verdadeira, o IMC é >= 40
    else:
        return "Obesidade grau III (mórbida)"


# ============================================================================
# FUNÇÃO PARA VALIDAR A ENTRADA DO USUÁRIO
# ============================================================================

def validar_numero(valor_str, nome_campo):
    """
    Função que tenta converter uma string para float e valida se é positiva
    
    Args:
        valor_str (str): string digitada pelo usuário
        nome_campo (str): nome do campo (para exibir na mensagem de erro)
    
    Returns:
        float: valor convertido e validado
    
    Exceções:
        ValueError: se a conversão falhar ou o valor for inválido
    """
    
    # Tenta converter a string para float
    # O bloco try/except captura erros de conversão (ex: usuário digitou "abc")
    try:
        # Converte a string para número decimal (float)
        valor = float(valor_str)
        
        # Verifica se o valor é maior que zero
        if valor <= 0:
            # Se for menor ou igual a zero, levanta uma exceção com mensagem personalizada
            raise ValueError(f"{nome_campo} deve ser maior que zero.")
        
        # Verifica limites máximos razoáveis para evitar números absurdos
        if nome_campo == "Peso" and valor > 500:
            raise ValueError("Peso muito alto. O valor máximo aceito é 500 kg.")
        
        if nome_campo == "Altura" and valor > 2.5:
            raise ValueError("Altura muito alta. O valor máximo aceito é 2.5 m.")
        
        # Se passou por todas as validações, retorna o valor
        return valor
    
    # Captura o erro caso a conversão falhe (usuário digitou letras, símbolos, etc)
    except ValueError as e:
        # Se a mensagem de erro já é a nossa personalizada (com nome_campo), relança
        # Caso contrário, adiciona uma mensagem genérica
        if "deve ser maior" in str(e) or "muito alto" in str(e):
            raise e
        else:
            raise ValueError(f"{nome_campo} inválido. Digite um número (ex: 70.5)")


# ============================================================================
# FUNÇÃO PRINCIPAL (MAIN) - ONDE A MÁGICA ACONTECE
# ============================================================================

def main():
    """
    Função principal que orquestra toda a execução do programa
    Exibe mensagens, captura entradas do usuário, chama as funções de cálculo
    e exibe o resultado final.
    """
    
    # Exibe um cabeçalho bonito para o usuário
    # A sequência "=" * 50 cria uma linha com 50 caracteres "="
    print("\n" + "=" * 50)
    print("      CALCULADORA DE IMC - VERSÃO TERMINAL")
    print("=" * 50)
    
    # Exibe uma explicação do que é IMC
    print("\nO Índice de Massa Corporal (IMC) é uma medida internacional")
    print("usada para calcular se uma pessoa está no peso ideal.")
    print("\nFórmula: IMC = peso (kg) / (altura (m) x altura (m))")
    print("-" * 50)
    
    # ========================================================================
    # CAPTURA DO PESO
    # ========================================================================
    
    # Loop infinito que só termina quando o usuário digitar um valor válido
    while True:
        # Solicita que o usuário digite o peso
        # input() exibe a mensagem e espera o usuário digitar e pressionar Enter
        peso_str = input("\nDigite seu peso (kg): ").strip()
        # .strip() remove espaços em branco no início e fim da string
        
        try:
            # Chama a função de validação para verificar se o peso é válido
            peso = validar_numero(peso_str, "Peso")
            # Se chegou aqui sem erro, o peso é válido
            break  # Sai do loop while
            
        except ValueError as erro:
            # Se ocorreu um erro, exibe a mensagem e o loop continua
            print(f"❌ Erro: {erro}")
            print("   Tente novamente.")
    
    # ========================================================================
    # CAPTURA DA ALTURA
    # ========================================================================
    
    # Loop infinito para capturar a altura
    while True:
        # Solicita que o usuário digite a altura
        altura_str = input("\nDigite sua altura (m): ").strip()
        
        try:
            # Chama a função de validação para verificar se a altura é válida
            altura = validar_numero(altura_str, "Altura")
            # Se chegou aqui sem erro, a altura é válida
            break  # Sai do loop while
            
        except ValueError as erro:
            # Se ocorreu um erro, exibe a mensagem e o loop continua
            print(f"❌ Erro: {erro}")
            print("   Tente novamente.")
    
    # ========================================================================
    # CÁLCULO E EXIBIÇÃO DO RESULTADO
    # ========================================================================
    
    # Chama a função de cálculo passando peso e altura como argumentos
    imc = calcular_imc(peso, altura)
    
    # Chama a função de classificação passando o IMC calculado
    classificacao = classificar_imc(imc)
    
    # Exibe uma linha separadora
    print("\n" + "=" * 50)
    print("                 R E S U L T A D O")
    print("=" * 50)
    
    # Exibe os dados de entrada
    print(f"\n📊 Dados informados:")
    print(f"   • Peso: {peso:.1f} kg")    # :.1f formata com 1 casa decimal
    print(f"   • Altura: {altura:.2f} m")  # :.2f formata com 2 casas decimais
    
    # Exibe o resultado do cálculo
    print(f"\n📐 Cálculo do IMC:")
    print(f"   IMC = {peso:.1f} / ({altura:.2f}²)")
    print(f"   IMC = {peso:.1f} / {altura * altura:.4f}")
    print(f"   IMC = {imc:.2f}")  # :.2f formata o IMC com 2 casas decimais
    
    # Exibe a classificação com um emoji indicador
    print(f"\n📋 Classificação (segundo a OMS):")
    
    # Adiciona um emoji diferente para cada classificação
    if "Abaixo" in classificacao:
        print(f"   ⚠️  {classificacao}")
    elif "normal" in classificacao:
        print(f"   ✅ {classificacao}")
    elif "Sobrepeso" in classificacao:
        print(f"   ⚠️  {classificacao}")
    else:
        print(f"   🔴 {classificacao}")
    
    # Exibe uma mensagem de orientação baseada na classificação
    print("\n💡 Orientação:")
    if imc < 18.5:
        print("   Consulte um nutricionista para ganho de peso saudável.")
    elif imc < 25:
        print("   Parabéns! Mantenha hábitos saudáveis.")
    elif imc < 30:
        print("   Considere aumentar atividade física e melhorar alimentação.")
    elif imc < 35:
        print("   Procure orientação médica para evitar complicações.")
    else:
        print("   ⚠️  Busque acompanhamento médico urgentemente!")
    
    # Exibe uma linha separadora final
    print("\n" + "=" * 50)
    print("         Obrigado por usar a calculadora!")
    print("=" * 50 + "\n")


# ============================================================================
# PONTO DE ENTRADA DO PROGRAMA
# ============================================================================

# Esta condição verifica se o script está sendo executado diretamente
# (e não importado como módulo por outro programa)
# __name__ é uma variável especial do Python
# Quando o script é executado diretamente, __name__ vale "__main__"
if __name__ == "__main__":
    # Chama a função principal para iniciar o programa
    main()
    
    # O programa só chega aqui depois que a função main() terminar
    # sys.exit(0) indica que o programa terminou com sucesso (código 0)
    sys.exit(0)