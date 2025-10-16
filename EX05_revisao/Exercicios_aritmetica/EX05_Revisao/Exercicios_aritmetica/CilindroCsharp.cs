using System;

namespace AreaCilindro
{
    class Program
    {
        static void Main(string[] args)
        {
            // Declaração das variáveis
            double raio, altura, area;

            // Entrada de dados
            Console.Write("Digite o raio do cilindro: ");
            raio = Convert.ToDouble(Console.ReadLine());

            Console.Write("Digite a altura do cilindro: ");
            altura = Convert.ToDouble(Console.ReadLine());

            // Verificação de valores válidos
            if (raio <= 0 || altura <= 0)
            {
                Console.WriteLine("❌ Erro: O raio e a altura devem ser maiores que zero.");
            }
            else
            {
                // Cálculo da área total do cilindro
                area = 2 * Math.PI * raio * (raio + altura);

                // Saída do resultado
                Console.WriteLine($"✅ A área total do cilindro é: {area:F2}");
            }

            // Espera o usuário pressionar uma tecla antes de encerrar
            Console.WriteLine("\nPressione qualquer tecla para sair...");
            Console.ReadKey();
        }
    }
}