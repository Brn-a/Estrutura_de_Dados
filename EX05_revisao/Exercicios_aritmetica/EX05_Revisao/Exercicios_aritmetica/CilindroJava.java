package com.mycompany.areacilindro;
import java.util.Scanner;

public class AreaCilindro {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        // Declaração de variáveis
        double raio, altura, area;

        // Entrada de dados
        System.out.print("Digite o raio do cilindro: ");
        raio = entrada.nextDouble();

        System.out.print("Digite a altura do cilindro: ");
        altura = entrada.nextDouble();

        // Verificação de valores válidos
        if (raio <= 0 || altura <= 0) {
            System.out.println("Erro: O raio e a altura devem ser maiores que zero.");
        } else {
            // Cálculo da área total do cilindro
            area = 2 * Math.PI * raio * (raio + altura);

            // Saída do resultado
            System.out.printf("A área total do cilindro é: %.2f\n", area);
        }

        entrada.close();
    }
}