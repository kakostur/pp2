//1 FizzBuzz

import UIKit

func FizzBuzz (number: Int) {
    if (number%3==0 && number%5==0){
        print ("FizzBuzz")
    }
    else if(number%5==0){
        print("Buzz")
    }
    else if(number%3==0){
        print("Fizz")
    }
    else{
        print("just number")
    }
}

for i in 1...100 {
    FizzBuzz(number: i)
}

FizzBuzz(number: 11)





//2 Prime Numbers

import Foundation

// Function to check if a number is prime
func isPrime(_ number: Int) -> Bool {
    if number <= 1 {
        return false
    }
    for i in 2..<number {
        if number % i == 0 {
            return false
        }
    }
    return true
}

//print primes between 1 and 100
for num in 1...100 {
    if isPrime(num) {
        print(num)
    }
}

isPrime(77)





//3 Temperature Converter

func celciusToKelvin (_ c : Double) -> Double {
    return (c + 273.15)
}
celciusToKelvin(14)

func celciusToFahrenheit (_ c : Double) -> Double {
    return c * 9/5 + 32
}
celciusToFahrenheit(10)

func fahrenheitToCelcius (_ f : Double) -> Double {
    return (f - 32) * 5/9
}
fahrenheitToCelcius(50)

func fahrenheitToKelvin (_ f : Double) -> Double{
    return (f - 32) * 5/9 + 273.15
}
fahrenheitToKelvin(20)

func kelvinToCelcius (_ k : Double) -> Double{
    return k - 273.15
}
kelvinToCelcius(290)

func kelvinToFahrenheit(_ k: Double) -> Double {
    return (k - 273.15) * 9/5 + 32
}
kelvinToFahrenheit(390)








//4 Shopping list
var shoppingList: [String] = [] //create an empty array

@MainActor func addItem (_ item: String) { //function that add items
    shoppingList.append(item)
    print ("Item was added ✅")
}

@MainActor func removeItem (_ item: String){ //function that delete the items
    if let index = shoppingList.firstIndex(of: item) {
        shoppingList.remove(at: index)
        print("Item was deleted ✅")
    }
    else{
        print("Item not founded 😔")
    }
}

@MainActor func ShowList () { //function that show shopping list with enumerated function
    if shoppingList.isEmpty{
        print("Your list is empty 🙌")
    }
    else{
        print("Shopping list: ")
        for (index, item) in shoppingList.enumerated(){
            print("\(index + 1). \(item)")
        }
    }
}

addItem("Bread")
removeItem("Bread")
ShowList()







//5 Word Frequency Counter

import Foundation

func wordFrequencyCounter(sentence: String) {
    //  Convert to lowercase (case-insensitive)
    let lowercased = sentence.lowercased()
    
    // Remove punctuation
    let cleaned = lowercased.components(separatedBy: CharacterSet.punctuationCharacters).joined()
    
    // Split into words
    let words = cleaned.split(separator: " ").map { String($0) }
    
    // Dictionary to store word counts
    var frequency: [String: Int] = [:]
    
    for word in words {
        frequency[word, default: 0] += 1
    }
    
    // Print result
    print(frequency)

}

let mySentence = "Hello, hello! This is a test"

wordFrequencyCounter(sentence: mySentence)








//6 Fibonacci Sequence

func fibonacci(_ n: Int) -> [Int] {
    //  Handle invalid cases
    if n <= 0 {
        return []
    }
    
    // Handle base cases
    if n == 1 {
        return [0]
    }
    if n == 2 {
        return [0, 1]
    }
    
    // Create an array with the first two numbers
    var sequence = [0, 1]
    
    // Loop to calculate the rest
    for i in 2..<n {
        let next = sequence[i - 1] + sequence[i - 2]
        sequence.append(next)
    }
    
    return sequence
}

print(fibonacci(7))






//7 Grade Calculator

func gradeCalculator(students: [String: Int]) {
    // Extract all scores
    let scores = Array(students.values)
    
    // Calculate average
    let total = scores.reduce(0, +)
    let average = Double(total) / Double(scores.count)
    
    // Find highest and lowest
    if let highest = scores.max(), let lowest = scores.min() {
        print(" Average Score: \(average)")
        print("Highest Score: \(highest)")
        print("Lowest Score: \(lowest)")
    }
    
    print("\n--- Student Results ---")
    
    // Loop through each student
    for (name, score) in students {
        let status = Double(score) >= average ? "✅ Above or equal to average" : "❌ Below average"
        print("\(name): \(score) \(status)")
    }

}

let studentScores = [
    "Merey": 85,
    "Miras": 70,
    "Karakat": 92,
    "Diana": 60,
    "Arman": 78
]

gradeCalculator(students: studentScores)








//8 Palindrom Checker
func isPalindrome(_ text: String) -> Bool {
    // Convert to lowercase
    let lowercased = text.lowercased()
    
    // Manually remove everything except letters and digits
    var cleaned = ""
    for char in lowercased {
        if (char >= "a" && char <= "z") || (char >= "0" && char <= "9") {
            cleaned.append(char)
        }
    }
    
    // Manually reverse the string
    var reversed = ""
    for char in cleaned {
        reversed = String(char) + reversed
    }
    
    // Compare cleaned with reversed
    return cleaned == reversed
}

let sentence = "Hello"
if isPalindrome(sentence) {
    print("✅ '\(sentence)' is a palindrome")
} else {
    print("❌ '\(sentence)' is not a palindrome")
}



//9 Simple Calculator
// Functions for each operation
func add(_ a: Double, _ b: Double) -> Double {
    return a + b
}

func subtract(_ a: Double, _ b: Double) -> Double {
    return a - b
}

func multiply(_ a: Double, _ b: Double) -> Double {
    return a * b
}

func divide(_ a: Double, _ b: Double) -> Double? {
    if b == 0 {
        return nil
    }
    return a / b
}
// Calculator function
func calculator() {
    let numbers: [(Double, Double, String)] = [
        (10, 5, "+"),
        (10, 5, "-"),
        (10, 5, "*"),
        (10, 0, "/"),
        (12, 3, "/")
    ]
    
    print("Calculator Results ")
    
    for (index, (a, b, operation)) in numbers.enumerated() {
        print("\n[\(index + 1)] Calculating: \(a) \(operation) \(b)")

        var result: Double?
        
        switch operation {
        case "+":
            result = add(a, b)
        case "-":
            result = subtract(a, b)
        case "*":
            result = multiply(a, b)
        case "/":
            result = divide(a, b)
            if result == nil {
                print("Error: Division by zero is not allowed")
                continue
            }
        default:
            print("Error: Unknown operation '\(operation)'")
            continue
        }
        
        if let value = result {
            print("Result: \(a) \(operation) \(b) = \(value)")
        }
    }
    
    print("\n All calculations completed ")
}

calculator()




//10 Unique Characters
// Function to check if all characters in a string are unique
func hasUniqueCharacters(_ text: String) -> Bool {
    // Create an empty Set
    var seenCharacters: Set<Character> = []
    
    // Loop through each character in the string
    for char in text {
        if seenCharacters.contains(char) {
            return false
        }
        seenCharacters.insert(char)
    }
    
    // If we never found duplicates, return true
    return true
}

let test1 = "Swift"
let test2 = "Hello"

print("Does '\(test1)' have all unique characters? \(hasUniqueCharacters(test1))")
print("Does '\(test2)' have all unique characters? \(hasUniqueCharacters(test2))")
