def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    males = int(input('Enter the number of males:'))
    females = int(input('Enter the number of females:'))
    total = int(males+females)
    print(f'The total is {total}')
    print(f'The number of males and females: {males} \t {females}')
    m_perc = (males/total)*100
    f_perc = (females/total)*100
    print(f'The percentage of males and females: {m_perc:.2f} \t {f_perc:.2f}')
    
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
