## makeCacheMatrix is a function that creates a list of functions on a special matirx to
## set the value of the matrixx
## get the value of the matrix
## set the value of the inverse
## get the value of the inverse

makeCacheMatrix <- function(x = matrix()) {
  
  inv <- NULL
  set <- function(y) {
    x <<- y
    m <<- NULL
  }
  get <- function() x
  setinv <- function(inverse) inv <<- inverse
  getinv <- function() inv
  list(set = set, get = get,
       setinv = setinv,
       getinv = getinv)

}


## The following function calculates the inverse of the special "marirx"
## created with the makeCacheMatrix. It first checks to see if the
## mean has already been calculated. If so, it get`s the inverse from the
## cache and skips the computation. Otherwise, it calculates the inverse

cacheSolve <- function(x, ...) {
        ## Return a matrix that is the inverse of 'x'
		inv <- x$getinv() ##checking for the existence of inverse
            if(!is.null(inv)) {
                    message("getting cached data")
                    return(inv) ## returning the cached inverse
            }
            data <- x$get() 
            inv <- solve(data) ## calculating the inverse
            x$setinv(inv)
            inv
}