use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::collections::HashMap;

fn main() {
    let file_path = "p1.txt";
    let scores = HashMap::from([
        ("A", 1),
        ("B", 2),
        ("C", 3),
        ("X", 1),
        ("Y", 2),
        ("Z", 3)
    ]);
    let mut myscore = 0;

    if let Ok(lines) = read_lines(file_path) {
        // Consumes the iterator, returns an (Optional) String
        for line in lines {
            let mut temp = 0;
            if let Ok(val) = line {
                println!("{}", val);
                let plays: Vec<_> = val.split(" ").collect();
                let trs = scores.get(plays[0]).unwrap();
                let outcome = plays[1];
                let mrs;
                if outcome == "X" {
                    if *trs == 3 {
                        mrs = 2;
                    } else if *trs == 2 {
                        mrs = 1;
                    } else {
                        mrs = 3;
                    }
                } else if outcome == "Z" {
                    if *trs == 3 {
                        mrs = 1;
                    } else if *trs == 2 {
                        mrs = 3;
                    } else {
                        mrs = 2;
                    }
                } else {
                    mrs = *trs;
                }
                
                
                temp += mrs;
                if (mrs == 1 && *trs == 3) || (mrs == 2 && *trs == 1) || (mrs == 3 && *trs == 2) {
                    temp += 6;
                } else if (*trs == 1 && mrs == 3) || (*trs == 2 && mrs == 1) || (*trs == 3 && mrs == 2) {
                    temp += 0;
                } else {
                    println!("{mrs} {trs}");
                    temp += 3;
                }

            }
            println!("{}", temp);
            myscore += temp;
        }
    }
    
    println!("{}", myscore);
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
