class ResponseResult:
    """
     Container of results for class Response

    """
    def __init__(self,
        A,
        B,
        C = None,
        D = None,
        U = None,
        t = None,
        y = None,
        _ = None,
        Vd = None,
        Vn = None,
    ):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.U = U
        self.t = t
        self.y = y
        self._ = _
        self.Vd = Vd
        self.Vn = Vn