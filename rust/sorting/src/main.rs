extern crate rand;

fn selection_sort(mut vec: Vec<u32>) -> Vec<u32> {
    println!("Beginning Selection Sort...");
    for i in 0..vec.len() {
        let mut min = i;
        for j in i..vec.len() {
            if vec[j] < vec[min] {
                min = j
            }
        }
        vec.swap(i,min);
    }
    vec
}

fn main() {
    println!("Rust - Sorting");
    println!("Generating random array...");

    let mut vec: Vec<u32> = Vec::with_capacity(32);

    for _ in 1..32 {
        vec.push(rand::random::<u32>() % 100);
    }

    println!("{:?}",vec);

    vec = selection_sort(vec);
    println!("{:?}",vec);
}
