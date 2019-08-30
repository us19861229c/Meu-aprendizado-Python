#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
026: Faça um programa que leia uma frase pelo teclado e mostre:
- quantas vezes aparece a letra "A/a";
- em que posição ela aparece a primeira vez e;
- em que posição ela aparece a última vez.
'''
frase = str(input("Digite uma frase: ")).strip().lower()

qnta = frase.count("a")
print(f"Quantas vezes a letra A aparece? "
      f"\nEla aparece {qnta} vezes")
primposi = frase.find("a")
print(f"Ela aparece pela primeira vez na posição {primposi}")
ultimposi = len(frase) - frase[::-1].find('a') - 1
print(f"Ela aparece pela última vez na posição {ultimposi}")



