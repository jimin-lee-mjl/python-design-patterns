# 팩토리 메서드 패턴
→ 팩토리란? <br />
→ 왜 팩토리를 사용하는가? <br />

<br />

### 의미

- 팩토리 : 객체의 생성을 위임받은 메서드/클래스
- 객체가 생성되는 곳과 객체가 사용되는 곳을 분리 → 왜?

<br />

### 왜 사용하는가?

클래스(컴포넌트)의 독립성 확보를 위해 

→ 하나의 컴포넌트가 다른 컴포넌트에 의존하고 있을 때, 이 의존성을 제거해야 독립성이 확보됨

→ 의존성을 제거하기 위해 사용하는 방법 : 의존성 역전 **(**dependency inversion**)**

→ 팩토리는 의존성 역전을 위해 사용됨

<br />

### 예시 코드 해설 
[v1.py](https://github.com/jimin-lee-mjl/python-design-patterns/blob/master/Factory_method/v1.py)
- 포켓볼 클래스는 피카츄 클래스, 파이리 클래스 등의 구상 클래스에 직접 의존
- 포켓볼 클래스는 피카츄, 파이리 등의 Concrete Product를 직접 생성
- 의존 관계 : class 포켓볼 → class 피카츄

[v2.py](https://github.com/jimin-lee-mjl/python-design-patterns/blob/master/Factory_method/v2.py)
- 포켓볼 클래스 → 구상 클래스들에 대한 의존성이 사라짐
- 포켓볼 클래스의 get_pokemon() 메서드는 포켓몬 추상 인터페이스를 참조
- 의존 관계 : class 포켓볼 → class 포켓몬 ← class 피카츄 (의존성 역전)
- 의존성 역전 원칙 → 추상에 의존하고 구체에는 의존하지 X
- 포켓볼 클래스는 이제 포켓몬팩토리에 직접 의존하게 됨

[v3.py](https://github.com/jimin-lee-mjl/python-design-patterns/blob/master/Factory_method/v3.py)
- 포켓볼 클래스는 이제 팩토리 클래스에도 의존하지 않는 대신 팩토리 메서드에서 포켓몬 생성과 관련한 모든 옵션을 제어하게 됨
- 팩토리 메서드에 관한 의존성도 완전히 제거하고 싶다면 '의존성을 주입(dependency injection)'해서 해결할 수 있음

<br />
💬 의존성 주입 : 의존하는 모듈을 메서드 내부에서 제거하고 인자로 받는 것
<br />
<br />
<br />

## 📚 Reference

- [https://jusungpark.tistory.com/14](https://jusungpark.tistory.com/14)
- [https://develogs.tistory.com/19](https://develogs.tistory.com/19)