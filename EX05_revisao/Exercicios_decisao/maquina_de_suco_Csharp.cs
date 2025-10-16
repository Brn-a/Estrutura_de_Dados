using System;

class MaquinaDeSucosSwitch
{
    static void Main(string[] args)
    {
        Console.WriteLine("--- BEM-VINDO À MÁQUINA DE SUCOS ---");
        Console.WriteLine("[1] Suco de Uva, [2] Suco de Maçã, [3] Suco de Laranja");
        Console.Write("Digite o número da opção desejada: ");
        int opcao = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine();

        switch (opcao)
        {
            case 1:
                Console.WriteLine("Você escolheu Suco de Uva. Ótima escolha, é refrescante!");
                break; 

            case 2:
                Console.WriteLine("Você escolheu Suco de Maçã. Um clássico!");
                break;

            case 3:
                Console.WriteLine("Você escolheu Suco de Laranja. Rico em vitamina C!");
                break;

            default:
                Console.WriteLine("Opção inválida! Por favor, escolha um número de 1 a 3.");
                break;
        }

        Console.WriteLine("\nObrigado por usar nossa máquina!");
    }
}