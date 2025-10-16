import java.util.Random;
import java.util.Scanner;

public class AdivinheONumero {
    public static void main(String[] args) {
        Random random = new Random();
        Scanner leitor = new Scanner(System.in);

        int numeroSecreto = random.nextInt(100) + 1; 
        int palpite = 0;

        System.out.println("--- JOGO: ADIVINHE O NUMERO ---");
        System.out.println("Eu escolhi um numero entre 1 e 100. Tente adivinhar!");

        while (palpite != numeroSecreto) {
            System.out.print("\nQual e o seu palpite? ");
            palpite = leitor.nextInt();

            if (palpite < numeroSecreto) {
                System.out.println("Muito baixo! Tente um numero maior.");
            } else if (palpite > numeroSecreto) {
                System.out.println("Muito alto! Tente um numero menor.");
            }
        }

        System.out.println("\nParabens! Voce acertou! O numero era " + numeroSecreto + ".");
        leitor.close();
    }
}