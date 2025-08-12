function createTrieNode() {
    return {
        children: new Map(),
        subTreeWordCount: 0
    };
}

function insert(root, word) {
    let node = root;
    node.subTreeWordCount++;
    for (const char of word) {
        if (!node.children.has(char))
            node.children.set(char, createTrieNode());
        node = node.children.get(char);
        node.subTreeWordCount++;
    }
}

function countWordsWithPrefix(root, prefix) {
    let node = root;
    for (const char of prefix) {
        if (!node.children.has(char))
            return 0;
        node = node.children.get(char);
    }
    return node.subTreeWordCount;
}

function solution(n, bans) {
    // 1. 전처리 : 삭제된 주문들을 길이에 따라 분류
    const bansByLength = new Map();
    for (let i=1 ; i<=11 ; i++) {
        bansByLength.set(i, []);
    }
    for (const ban of bans) {
        if (ban.length <= 11)
            bansByLength.get(ban.length).push(ban);
    }

    let targetLength = 0;
    let n_big = BigInt(n);

    // 2. 정답 주문의 길이 찾기
    for (let len=1 ; len<=11 ; len++) {
        const totalInLength = 26n ** BigInt(len);
        const bannedInLength = BigInt(bansByLength.get(len).length);
        const validInLength = totalInLength - bannedInLength;

        if (n_big <= validInLength) {
            targetLength = len;
            break;
        } else {
            n_big -= validInLength;
        }
    }

    // 3. 트라이 루트 노드 생성 및 해당 길이의 삭제된 주문 삽입
    const trieRoot = createTrieNode();
    const targetBans = bansByLength.get(targetLength);
    for (const ban of targetBans) {
        insert(trieRoot, ban);
    }

    let answer = "";

    // 4. 정답 주문의 '문자' 하나씩 찾기
    for (let i=0 ; i<targetLength ; i++) {
        for (let j=0 ; j<26 ; j++) {
            const char = String.fromCharCode('a'.charCodeAt(0) + j);
            const currentPrefix = answer + char;
            const remainingLength = targetLength - currentPrefix.length;

            // 현재 접두사로 만들 수 있는 총 단어 수
            const totalWordsInSubtree = 26n ** BigInt(remainingLength);
            // 현재 접두사로 시작하는 삭제된 단어 수 (트라이에서 조회)
            const bannedWordsInSubtree = BigInt(countWordsWithPrefix(trieRoot, currentPrefix));
            // 현재 접두사로 만들 수 있는 유효한 단어 수
            const validWordsInSubtree = totalWordsInSubtree - bannedWordsInSubtree;

            if (n_big <= validWordsInSubtree) {
                answer += char;
                break; // 현재 자리의 문자 확정, 다음 자리로 이동
            } else {
                n_big -= validWordsInSubtree;
            }
        }
    }

    return answer;
}