(define filename "input.scm")
(define in (open-input-file filename))
(define data (read in))
(close-input-port in)

(define (mass-to-fuel mass)
  (- (floor (/ mass 3)) 2))

(define (sum numbers)
  (if (null? numbers) 0
    (+ (car numbers) (sum (cdr numbers)))))

(define (calc-fuel mass)
  (if (<=  mass 0) 0
    (+ (max (mass-to-fuel mass) 0) (calc-fuel (mass-to-fuel mass)))))

(display (sum (map (lambda (num)
	      (calc-fuel num)) data)) (current-output-port))
(newline)
