
Program developed for Reading, Analysis, Processing and Ploting of CTD data  

Github repository website: 
			
			http: https://github.com/rsoutelino/uerj_ocn_2014.git
			ssh: git@github.com:rsoutelino/uerj_ocn_2014.git 
			Subversion: https://github.com/rsoutelino/uerj_ocn_2014

Written for the course "Reading, Analysis and Processing of Scientific Data using Python" 
State University of Rio de Janeiro 
Supervisor: Dr. Rafael Soutelino

   
Date: 27 - 28/nov/2014


Written by Bruno Fonseca (brunofonseca570@gmail.com)
           Camila Guedes Viana (cgv.camila@gmail.com)
           Fernanda Moreira Rêgo (fe.moreira91@gmail.com)
           Helen Soares (helensoares@gmail.com)
           Douglas Medeiros Nehme (medeiros.douglas3@gmail.com)
           Anna Bia (oaquim.bia@gmail.com)
           Talitha (talitha.sl@gmail.com)
           Phellipe Couto (phellipe.couto@gmail.com)
           Vanessa Bach (vanessabach.r@gmail.com)
           Gabriela Nalini (gabrielanalini@gmail.com)
           Ana Paula (apmdoin@gmail.com)


Library Requirement: 
          argparser
          matplotlib.pyplot as plt

Description library used:
          argparser: used to interpret the arguments.
          matplotlib.pyplot: plot data

This module can load SeaBird CTD (CNV)
  Input CTD data are in .cnv format 
Example: ctd_bruto.cnv 

  Output data are in .txt format
Example: ctd_tratado.txt 


Contents: 

i. Data reading

1. Download the ctd_bruto.csv file, and put it in the working directory.
2. Import file and extract data from ctd_bruto.csv

f=open ('data/ctd_bruto.cnv')

3. Establish header and data
    (Exemplo em construção)

4. Create variables 
press = []
temp1 = [] 
temp2 = []


ii. Data processing

Identifying spurious data, fixing gaps, interpolating and creating a trated serie.

iii. Data plot

iv. Output Data









