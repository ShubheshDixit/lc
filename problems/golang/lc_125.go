package main

import "fmt"

func isAlphanumeric(c rune) bool {
	return (c >= 'a' && c <= 'z') || (c >= '0' && c <= '9') || (c >= 'A' && c <= 'Z')
}

func isSame(a, b rune) bool {
	if a >= 'A' && a <= 'Z' {
		a += 'a' - 'A'
	}
	if b >= 'A' && b <= 'Z' {
		b += 'a' - 'A'
	}
	return a == b
}

func isPalindrome(s string) bool {
	if len(s) == 0 {
		return true
	}
	word := []rune(s)
	left, right := 0, len(word)-1
	for left < right {
		if !isAlphanumeric(word[left]) {
			left++
			continue
		}
		if !isAlphanumeric(word[right]) {
			right--
			continue
		}
		if !isSame(word[left], word[right]) {
			return false
		}
		left++
		right--
	}
	return true
}

func main() {
	s := "race a car"
	fmt.Println(isPalindrome(s))
}
