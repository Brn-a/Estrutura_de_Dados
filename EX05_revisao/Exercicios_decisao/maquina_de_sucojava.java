import java.util.Scanner;

public class MaquinaDeSucosIf {
    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);
        int opcao;

        System.out.println("--- BEM-VINDO A MAQUINA DE SUCOS ---");
        System.out.println("[1] Suco de Uva, [2] Suco de Maca, [3] Suco de Laranja");
        System.out.print("Digite o numero da opcao desejada: ");
        opcao = leitor.nextInt();
        System.out.println();

        if (opcao == 1) {
            System.out.println("Voce escolheu Suco de Uva. Otima escolha, e refrescante!");
        } else if (opcao == 2) {
            System.out.println("Voce escolheu Suco de Maca. Um classico!");
        } else if (opcao == 3) {
            System.out.println("Voce escolheu Suco de Laranja. Rico em vitamina C!");
        } else {
            System.out.println("Opcao invalida! Por favor, escolha um numero de 1 a 3.");
        }

        System.out.println("\nObrigado por usar nossa maquina!");
        leitor.close();
    }
}