(define filename "input.scm")
(define in (open-input-file filename))
(define data (read in))
(close-input-port in)

(define (sum numbers)
  (if (null? numbers) 0
    (+ (car numbers) (sum (cdr numbers)))))

(display (sum (map (lambda (num)
	      (- (floor (/ num 3)) 2)) data)) (current-output-port))
