fn main() {
    println!("Hello, world!");
    // read file 
    let contents = std::fs::read_to_string("src/input1.txt").unwrap();
    // define a 2d vector to keep list of all double lines
    let mut idx = 0;
    let mut line_int = 0;
    let mut sum_vec: Vec<i32> = Vec::new();

    
    contents.lines().for_each(|line|{
        if line == ""{
            idx+= 1;
            sum_vec.push(line_int);
            line_int = 0;

        }
        else {
            line_int += line.parse::<i32>().unwrap();
            // println!("Int Line {intLine}");
        }
    });
    sum_vec.push(line_int);
    println!("ID:{}, MaxSum: {:?}",idx+1, sum_vec.iter().max().unwrap());
}
