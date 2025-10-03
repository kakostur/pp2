import Foundation

//  Personal Information
var firstName: String = "Karakat"
var lastName: String = "Tursynbaeva"
let birthYear: Int = 2005
let currentYear: Int = 2025
var age: Int = currentYear - birthYear
var isStudent: Bool = true
var height: Double = 1.55
var country: String = "Kazakhstan"
var favoriteEmoji: String = "💫"

//  Hobbies and Interests
var hobby: String = "Reading 📚"
var numberOfHobbies: Int = 4
var favoriteNumber: Int = 5
var isHobbyCreative: Bool = true
var secondHobby: String = "Watching movies 💻"
var thirdHobby: String = "Traveling ✈️"

//  Future Goals
var futureGoals: String = "In the future, I want to become a successful software engineer 👩‍💻 and travel the world 🌍."

// Combine into a Life Story
var lifeStory: String = """
My name is \(firstName) \(lastName). I am \(age) years old, born in \(birthYear).
I live in \(country). My height is \(height)m. Favorite emoji: \(favoriteEmoji).
Am I a student? \(isStudent ? "Yes 🎓" : "No ❌").

My favorite hobby is \(hobby), which is \(isHobbyCreative ? "a creative hobby" : "not very creative").
I also enjoy \(secondHobby) and \(thirdHobby). In total, I have \(numberOfHobbies) hobbies.
My favorite number is \(favoriteNumber).

\(futureGoals)
"""

print(lifeStory)
