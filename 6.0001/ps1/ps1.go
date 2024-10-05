package main

import (
	"fmt"
	"math"
	"os"
)

func main() {
	ps1a()
	ps1b()
	ps1c()
}

func ps1a() {
	const portionDownPayment = 0.25
	const interestRate = 0.04

	var annualSalary, portionSaved, totalCost float64

	fmt.Print("Enter your annual salary: ")
	fmt.Scan(&annualSalary)

	fmt.Print("Enter the percent of your salary to save, as a decimal: ")
	fmt.Scan(&portionSaved)

	fmt.Print("Enter the cost of your dream home: ")
	fmt.Scan(&totalCost)

	downPaymentRequired := portionDownPayment * totalCost

	currentSavings := 0.0

	months := 0
	for currentSavings <= downPaymentRequired {
		currentSavings += currentSavings * interestRate / 12.0
		currentSavings += annualSalary * portionSaved / 12.0
		months += 1
	}

	fmt.Println("Months", months)

}

func ps1b() {
	const portionDownPayment = 0.25
	const interestRate = 0.04

	var annualSalary, portionSaved, totalCost, raise float64

	fmt.Print("Enter your annual salary: ")
	fmt.Scan(&annualSalary)

	fmt.Print("Enter the percent of your salary to save, as a decimal: ")
	fmt.Scan(&portionSaved)

	fmt.Print("Enter the cost of your dream home: ")
	fmt.Scan(&totalCost)

	fmt.Print("Enter the semi­annual raise, as a decimal: ")
	fmt.Scan(&raise)

	downPaymentRequired := portionDownPayment * totalCost

	currentSavings := 0.0

	months := 0
	for currentSavings <= downPaymentRequired {
		currentSavings += currentSavings * interestRate / 12.0
		currentSavings += annualSalary * portionSaved / 12.0
		months += 1
		if months%6 == 0 {
			annualSalary += annualSalary * raise
		}
	}

	fmt.Println("Months", months)

}

func ps1c() {
	const portionDownPayment = 0.25
	const raise = 0.07
	const interestRate = 0.04
	const totalCost = 1_000_000.0
	const epsilon = 100

	downPaymentRequired := portionDownPayment * totalCost

	var originalAnnualSalary float64

	fmt.Print("Enter your annual salary: ")
	fmt.Scan(&originalAnnualSalary)

	min, max := 1, 10_000

	steps := 0
	for math.Abs(float64(min)-float64(max)) > 1 {
		steps += 1

		var savingsRateGuess int = int((min + max) / 2)

		currentSavings := 0.0

		annualSalary := originalAnnualSalary

		for months := range 36 {
			currentSavings += currentSavings * interestRate / 12.0
			currentSavings += annualSalary * float64(savingsRateGuess) / 12.0 / 10000.0
			months += 1
			if months%6 == 0 {
				annualSalary += annualSalary * raise
			}
		}

		difference := math.Abs(currentSavings - downPaymentRequired)

		if difference <= epsilon {
			fmt.Printf("Best savings rate: %.4f\n", float64(savingsRateGuess)/10_000)
			fmt.Println("Steps in bisection search:", steps)
			os.Exit(0)
		} else if difference > epsilon && currentSavings > downPaymentRequired {
			max = savingsRateGuess
		} else if difference > epsilon && currentSavings < downPaymentRequired {
			min = savingsRateGuess
		}
	}

	fmt.Println("It is not possible to pay the down payment in three years.")
}
