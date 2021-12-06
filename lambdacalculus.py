zero = lambda f: lambda x: x
one = lambda f: lambda x: f(x)
two = lambda f: lambda x: f(f(x))
sucsessor = lambda n: lambda f: lambda x: f(n(f)(x))
predecesor = lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda u: x)(lambda x: x)

add = lambda m: lambda n: lambda f: lambda x: m(f)(n(f)(x))
sub = lambda m: lambda n: n(predecesor)(m)
mul = lambda m: lambda n: lambda f: m(n(f))
pow = lambda m: lambda n: lambda f: n(m)(f)

int_to_church = lambda n: zero if n == 0 else sucsessor(int_to_church(n - 1))
church_to_int = lambda n: n(lambda x: x + 1)(0)
