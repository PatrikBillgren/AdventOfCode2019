(define filename "input.scm")
(define in (open-input-file filename))
(define data (read in))
(close-input-port in)
(define program (list->vector data))

(define (apply-fun fun ref-one ref-two)
  (fun 
    (vector-ref program (vector-ref program ref-one))
    (vector-ref program (vector-ref program ref-two))
  )
)

(define (add-two ref-one ref-two)
  (apply-fun + ref-one ref-two)
)

(define (multiply-two ref-one ref-two)
  (apply-fun * ref-one ref-two)
)

(define (set index value)
  (vector-set! 
    program 
    (vector-ref program (+ index 3)) 
    value
  )
)


(define (int-code1 index)
  (set index (add-two (+ index 1) (+ index 2)))
)

(define (int-code2 index)
  (set index (multiply-two (+ index 1) (+ index 2)))
)

(define (run-code index)
  (begin 
    (if (= (vector-ref program index) 1) (int-code1 index)
      (if (= (vector-ref program index) 2) (int-code2 index))
    )
    (if (= (vector-ref program index) 99) 
      (vector-ref program 0) 
      (run-code (+ index 4))
    )
  )
)

(define (set-second-third sec thi)
  (vector-set! program 1 sec)
  (vector-set! program 2 thi)
)
 
(set-second-third 12 2)
(display (run-code 0) )
(newline)
