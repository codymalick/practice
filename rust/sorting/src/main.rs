mod algorithms;

extern crate rand;

use algorithms::selection;


fn main() {
    println!("Rust - Sorting");
    println!("Generating random array...");

    let mut vec: Vec<u32> = Vec::with_capacity(32);

    for _ in 1..32 {
        vec.push(rand::random::<u32>() % 100);
    }

    println!("{:?}",vec);

    vec = selection::selection_sort(vec);
    println!("{:?}",vec);
}
