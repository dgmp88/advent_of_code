use std::collections::HashMap;

fn string_to_vec(mem: &str) -> Vec<i32> {
    // Turn a string into a vec of vec of f32's
    let mut mem_vec = Vec::new();
    for block in mem.split(" ") {
        let int = block.trim().parse::<i32>();
        match int {
            Ok(val) => mem_vec.push(val),
            Err(_why) => {} ,
        }
    }
    mem_vec
}

fn count_cycles (mem: &mut Vec<i32>) -> (usize, usize) {
    let mut iteration = 0;
    let mut seen = HashMap::new();
    loop {
       iteration += 1; 
       seen.insert((*mem).clone(), iteration);
       allocate(mem);
       match seen.get(mem) {
        Some(x) => return (iteration, (iteration-x)+1),
        None => {},
       }
    }
}

fn allocate(mem: &mut Vec<i32>) {
    let (max_val, max_idx) = max(mem);
    mem[max_idx] = 0;
    for i in (max_idx+1)..(max_idx+1+(max_val as usize)) {
        let idx = i % mem.len();
        mem[idx] += 1;
    }
}

fn max(mem: &Vec<i32>) -> (i32, usize) {
    let mut max_idx = 0;
    let mut max_val = mem[max_idx];
    for i in 0..mem.len() {
        if mem[i] > max_val {
            max_val = mem[i];
            max_idx = i;
        }
    }
    (max_val, max_idx)
}

fn test() {
    let mem_str = "0 2 7 0";
    let mut mem = string_to_vec(mem_str);
    let cycles = count_cycles(&mut mem);
    let count = cycles.0;
    
    assert!(count == 5, "Test count should be 5, it is {}", count);
    
    let loop_count = cycles.1;
    assert!(loop_count == 4, "Test count should be 4, it is {}", loop_count);
}

fn get_mem() -> Vec<i32>{
    let mem = "11   11  13  7   0   15  5   5   4   4   1   1   7   1   15  11";
    string_to_vec(mem)
}

fn one() {
    let mut mem = get_mem();
    let count = count_cycles(&mut mem);
    println!("Result 1 is {}", count.0);
}

fn two() {
    let mut mem = get_mem();
    let count = count_cycles(&mut mem);
    println!("Result 2 is {}", count.1);
}

fn main() {
    test();
    one();
    two();
}


