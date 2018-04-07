pub fn selection_sort(mut vec: Vec<u32>) -> Vec<u32> {
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

#[cfg(test)]
mod test_selection_sort {
    use super::selection_sort;

    #[test]
    fn simple_case() {
        let inital_vec = vec![4, 3, 1, 2];
        let expected_vec = vec![1, 2, 3, 4];
        let result_vec = selection_sort(inital_vec);
        assert_eq!(expected_vec, result_vec)
    }

    #[test]
    fn sorted_input() {
        let inital_vec = vec![1, 2, 3, 4];
        let expected_vec = vec![1, 2, 3, 4];
        let result_vec = selection_sort(inital_vec);
        assert_eq!(expected_vec, result_vec)
    }
}