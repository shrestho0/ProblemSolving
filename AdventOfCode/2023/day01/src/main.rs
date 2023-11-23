use std::{fs, vec};

fn main() {
    // read contents from file
    let file_path = "src/input3.txt";
    let contents = fs::read_to_string(&file_path).unwrap();

    let mut num_vec: Vec<i32> = vec![];

    contents.lines().for_each(|line| {
        num_vec.push(two_digits_from_line(&line));
    });

    println!("{:?}", num_vec.iter().sum::<i32>());
}

fn two_digits_from_line(line: &str) -> i32 {
    println!("{:?}", line);
    let arr = [
        "nine", "eight", "seven", "six", "five", "four", "three", "two", "one",
    ];
    let arr2 = ["9", "8", "7", "6", "5", "4", "3", "2", "1"];

    // fix here, do it manually

    let mut new_line = String::from(line);

    for i in 0..10 {
        for j in 0..10 {
            todo!()
        }
    }

    // while i < arr.len() {
    //     new_line = new_line.replace(&arr[i], &arr2[i]);
    //     i += 1;
    // }

    let digit_string: Vec<char> = new_line.chars().filter(|pred| pred.is_digit(10)).collect();

    let mut number_digit = String::new();
    if digit_string.len() == 1 {
        number_digit.push(digit_string[0]);
        number_digit.push(digit_string[0]);
    } else {
        number_digit.push(digit_string[0]);
        number_digit.push(digit_string[digit_string.len() - 1]);
    }

    println!(
        "{:?} {:?} {:?} {:?}",
        line, new_line, digit_string, number_digit
    );

    return 69;
}

// fn two_digits_from_line(line: &str) -> i32 {
//     // let mut left_found = false;
//     // let mut right_found = false;

//     // word to number
//     println!("{:?}", word_to_digit(&line));

//     let digit_string: Vec<char> = line.chars().filter(|pred| pred.is_digit(10)).collect();
//     // println!("{} {:?}", line, digit_string);

//     return number_from_digits(&digit_string);
// }

// fn number_from_digits(digits: &Vec<char>) -> i32 {
//     let mut dstr = String::from("");
//     if digits.len() == 1 {
//         dstr.push(digits[0]);
//         dstr.push(digits[0]);
//     } else {
//         dstr.push(digits[0]);
//         dstr.push(digits[digits.len() - 1]);
//     }

//     return dstr.parse().unwrap();
// }

// fn word_to_digit(line: &str) -> String {
//     let arr = [
//         "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
//     ];
//     let mut new_line = String::new();

//     println!("{:?} {:?} ", line, new_line);

//     // for el in arr {
//     //     new_line = line.replace(&"two", "2")
//     // }

//     let mut i = 0;
//     while i < arr.len() {
//         i += 1;
//     }

//     return line.to_string();
// }
