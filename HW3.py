###############################################################################################
## Python 2 - Store Recept Calculator                                                        ##
##      Functions / IO                                                                       ##
##                                                                                           ##
## Your program will ask the user how many of each stock item they wish to purchase and      ##
## then print out a receipt regarding the purchases.                                         ##
##                                                                                           ##
## ==== Details ====                                                                         ##
## Your store will be selling the following items:                                           ##
## Video card   $399.99                                                                      ##
## Motherboard  $159.99                                                                      ##
## CPU          $539.99                                                                      ##
## Power Supply $129.99                                                                      ##
## RAM          $ 39.99                                                                      ##
## Bluray Drive $ 59.99                                                                      ##
## PC Case      $149.99                                                                      ##
## Monitor      $569.99                                                                      ##
##                                                                                           ##
## Your store will also calculate the total sales tax, at a rate of 11%.                     ##
##                                                                                           ##
## ==== Sample Input ====                                                                    ##
## Welcome to amazing store!                                                                 ##
## How many of the following do you wish to purchase?                                        ##
## Video card: 1                                                                             ##
## Motherboard: 1                                                                            ##
## CPU: 1                                                                                    ##
## Power Supply: 0                                                                           ##
## RAM: 4                                                                                    ##
## Bluray Drive: 0                                                                           ##
## PC Case: 0                                                                                ##
## Monitor: 0                                                                                ##
##                                                                                           ##
## ==== Sample Output ====                                                                   ##
## ===================================                                                       ##
## ==    Fantastic Store Receipt    ==                                                       ##
## ===================================                                                       ##
## ==   Video card      1   $399.99 ==                                                       ##
## ==   Motherboard     1   $159.99 ==                                                       ##
## ==   CPU             1   $539.99 ==                                                       ##
## ==   RAM             4   $159.96 ==                                                       ##
## ==                               ==                                                       ##
## ==   Sub Total          $1259.93 ==                                                       ##
## ==   Sales Tax           $138.59 ==                                                       ##
## ===================================                                                       ##
## ==   Total              $1398.52 ==                                                       ##
## ===================================                                                       ##
###############################################################################################

if __name__ == "__main__":
    # You code here