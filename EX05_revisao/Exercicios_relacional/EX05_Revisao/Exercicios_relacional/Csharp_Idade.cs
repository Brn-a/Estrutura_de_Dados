using System;

namespace ComparadorDeIdades
{
    class Program
    {
        static void Main(string[] args)
        {
            string nome1, nome2;
            int idade1, idade2;

            Console.Write("Digite o nome da primeira pessoa: ");
            nome1 = Console.ReadLine();

            Console.Write($"Digite a idade de {nome1}: ");
            idade1 = Convert.ToInt32(Console.ReadLine());

            Console.Write("Digite o nome da segunda pessoa: ");
            nome2 = Console.ReadLine();

            Console.Write($"Digite a idade de {nome2}: ");
            idade2 = Convert.ToInt32(Console.ReadLine());

            if (idade1 > idade2)
            {
                Console.WriteLine($"{nome1} é mais velho(a) que {nome2}.");
            }
            else if (idade1 < idade2)
            {
                Console.WriteLine($"{nome2} é mais velho(a) que {nome1}.");
            }
            else
            {
                Console.WriteLine($"{nome1} e {nome2} têm a mesma idade.");
            }
        }
    }
}