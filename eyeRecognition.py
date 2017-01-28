def getGradients(Quads):
    """
    Input: a tuple of 4 quads.
    Output: a tuple of 4 lists
    - Each is a list of gradients
    """
    output = []
    for i in range(4):
        l = []
		if len(quads[i]) == 1:
			if i == 0:
				temp = quads[i+1][-1]
				l = [float(temp[1] - quads[i][0][1]) / temp[0] - quads[i][0][0]]
			elif i == 1:
				temp = quads[i-1][-1]
				l = [float(temp[1] - quads[i][0][1]) / temp[0] - quads[i][0][0]]
			elif i == 2:
				temp = quads[i+1][-1]
				l = [float(temp[1] - quads[i][0][1]) / temp[0] - quads[i][0][0]]
			elif i == 3:
				temp = quads[i-1][-1]
				l = [float(temp[1] - quads[i][0][1]) / temp[0] - quads[i][0][0]]

		else:
	        for j in range(len(Quads[i]) - 1):
				l.append(float(l[j+1][1]-l[j][1])/(l[j+1][0]-l[j][0]))
		output.append(l)
	return output


def getMaxX(l):
    m = 0
    v = None
    for (x, y) in l:
        if x >= m:
            m = x
            v = (x, y)
    return v

def getMinX(l):
    m = sys.maxint
    v = None
    for (x, y) in l:
        if x <= m:
            m = x
            v = (x, y)
    return v

def getEyeQuads(eye):
    ul = []
    ur = []
    ll = []
    lr = []

    (xmax, y1) = getMaxX(eye)
    (xmin, y2) = getMinX(eye)

    if xmax == None or xmin == None:
        print "xmax == None or xmin == None"
        return -1

    xmedian = (xmax + xmin) / 2.0
    ymedian = (y1 + y2) / 2.0

    for (x, y) in eye:
        if x > xmin and x < xmidian:
            if y > ymidian:
                ul.append((x, y))
            else:
                ll.append((x, y))
        else if x < xmax and x > xmedian:
            if y > ymidian:
                ur.append((x, y))
            else:
                lr.append((x, y))

    ul.append((xmin, y2))
    ll.append((xmin, y2))
    ur.append((xmax, y1))
    lr.append((xmax, y1))

    return [ur, ul, ll, lr]

def sort(l):
	for i in range(1, len(l)):
		tmp = l[i]
		k = i
		while k > 0 and tmp[0] < l[k - 1][0]:
			l[k] = l[k - 1]
			k -= 1
			l[k] = tmp

def compressData(l, a, b):
	out = []
	for i in range(0, a, b):
		s = 0
		for j in range(b):
			s += l[j]
		out.append(float(s)/b)
	return out

def eyeTypes(gradients):
	global trainingData

	eyeData = trainingData["eye"]

	totalScore = []
	for i in range(4):
		quad = gradients[i]
		score = {}
		for (t, d) in eyeData:
			s = 0
			if len(quad) < len(d):
				d = compressData(d, len(d), len(quad))
			elif len(quad) > len(d):
				quad = compressData(quad, len(quad), len(d))

			for j in range(min(len(quad), len(d))):
				if eyeData[i] > quad[j] - 0.15 and eyeData[i] < quad[j] - 0.15:
					s += 1

			score["t"] = float(s)/min(len(quad), len(d))
		totalScore.append(score)
	return totalScore


def getEyeType(eyeTypes):
	out = []
	types = {}
	for quad in eyeTypes:
		bestp = 0
		bestt = None
		secondp = 0
		secondt = None
		for t in (quad.keys()):
			p = quad[t]
			if p >= bestp:
				bestt = t
				bestp = p

		if bestt not in types:
			types[bestt] = (1, bestp, bestp)
		else:
			(a, b, c) = types[bestt]
			types[bestt] = (a+1, b+bestp, c+bestp / 2)


		for t in (quad.keys()):
			p = quad[t]
			if p >= secondp && t != bestt:
				secondt = t
				secondp = p

		if secondt not in types:
			types[secondt] = (1, secondp, secondp)
		else:
			(a, b, c) = types[secondt]
			types[secondt] = (a+1, b+secondp, c+secondp / 2)


		out.append([(bestt, bestp), (secondt, secondp)])

	best = None
	b = 0
	for t in (quad.keys()):
		if types[t] >= b:
			b = types[t]
			best = t

	second = None
	s = 0
	for t in (quad.keys()):
		if types[t] >= s and t != second:
			s = types[t]
			second = t

	return (best, second)

def eye(l):
	eyeQuads = getEyeQuads(l)

	for i in range(4):
		sort(eyeQuads[i])

	gradiants = getGradients(eyeQuads)
	eyeTypes = getEyeType(gradienst)

	return getEyeType(eyeTypes)

def getType(l, trainingData):
	global trainingData
	(eyel1, eyel2) = eye(l[0])
	(eyer1, eyer2) = eye(l[1])

	if eyel1 == eyer1:
		return eyel1
	elif eyel1 == eyer2:
		return eyel1
	elif eyel2 == eyer1:
		return eyer1
	elif eyel2 == eyer2:
		return eyel2
	else:
		return eyel1
