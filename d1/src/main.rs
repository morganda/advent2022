use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let file_path = "p1.txt";
    let mut highest = 0;
    let mut temp = 0;

    if let Ok(lines) = read_lines(file_path) {
        // Consumes the iterator, returns an (Optional) String
        for line in lines {
            if let Ok(val) = line {
                if val.is_empty() {
                    println!("{}", temp);
                    if temp > highest {
                        highest = temp;
                    }
                    temp = 0;
                } else {
                    let num = val.parse::<i32>().unwrap();
                    temp += num;
                }
            }
        }
    }
    
    println!("{}", highest);
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
