using System;

class AdivinheONumero
{
    static void Main(string[] args)
    {
        Random random = new Random();
        int numeroSecreto = random.Next(1, 101);
        int palpite = 0; 

        Console.WriteLine("--- JOGO: ADIVINHE O NUMERO ---");
        Console.WriteLine("Eu escolhi um numero entre 1 e 100. Tente adivinhar!");

       
        while (palpite != numeroSecreto)
        {
            Console.Write("\nQual e o seu palpite? ");
            palpite = Convert.ToInt32(Console.ReadLine());

            if (palpite < numeroSecreto)
            {
                Console.WriteLine("Muito baixo! Tente um numero maior.");
            }
            else if (palpite > numeroSecreto)
            {
                Console.WriteLine("Muito alto! Tente um numero menor.");
            }
        }

        Console.WriteLine($"\nParabens! Voce acertou! O numero era {numeroSecreto}.");
    }
}