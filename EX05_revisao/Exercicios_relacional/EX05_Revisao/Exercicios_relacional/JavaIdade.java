package com.mycompany.comparaidade;

import java.util.Scanner;

public class ComparaIdade {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        // Entrada dos dados
        System.out.print("Digite o nome da primeira pessoa: ");
        String nome1 = entrada.nextLine();

        System.out.print("Digite a idade de " + nome1 + ": ");
        int idade1 = entrada.nextInt();
        entrada.nextLine(); // limpa o buffer

        System.out.print("Digite o nome da segunda pessoa: ");
        String nome2 = entrada.nextLine();

        System.out.print("Digite a idade de " + nome2 + ": ");
        int idade2 = entrada.nextInt();

        // Comparação das idades
        if (idade1 > idade2) {
            System.out.println(nome1 + " é mais velho(a) que " + nome2 + ".");
        } 
        else if (idade1 < idade2) {
            System.out.println(nome2 + " é mais velho(a) que " + nome1 + ".");
        } 
        else {
            System.out.println(nome1 + " e " + nome2 + " têm a mesma idade.");
        }

        entrada.close();
    }
}
