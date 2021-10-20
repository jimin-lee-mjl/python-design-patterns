# Borg 패턴
→ Borg 패턴이란? <br />
→ 왜 Singleton 대신 Borg를 쓰는가? <br />
→ vs Singleton 패턴  <br />
→ vs Flyweight 패턴 <br />

<br />

## 개념 
클래스의 모든 인스턴스들이 동일한 상태(state)를 공유하는 디자인 패턴 ( == Monostate 패턴)
```python
class Borg(object):
  _shared_state = {}

  def __new__(cls, *args, **kwargs):
    obj = super(Borg, cls).__new__(cls, *args, **kwargs)
    obj.__dict__ = cls._shared_state
    return obj

OR 

class Borg:
    _shared_state = {}
    
    def __init__(self):
        self.__dict__ = self._shared_state


if __name__ == '__main__':
    b1 = Borg()
    b2 = Borg()

    print(b1 is b2) # False

    b1.name = 'Marie'
    print(b1.name)  # Marie
    print(b2.name)  # Marie

    b2.name = 'Emily'
    print(b1.name)  # Emily
    print(b2.name)  # Emily
```
- 일반적으로 파이썬 클래스의 인스턴스들의 상태(state)는 `__dict__()` 메서드를 통해 인스턴스 각각의 딕셔너리에 저장됨
- Borg 패턴에서는 인스턴스의 딕셔너리가 `_shared_state` 이라는 클래스 변수를 가리키도록 해놨기 때문에 모든 인스턴스가 동일한 딕셔너리를 사용하게 됨

<br />

## 왜 Singleton 대신 Borg를 쓰는가?

참고 : [http://www.aleax.it/Python/5ep.html](http://www.aleax.it/Python/5ep.html) 

- what is in an instance? → **identity**(id), **state**(attribute), **behavior**(method)
- behavior → 메서드는 기본적으로 인스턴스들 사이에서 공유됨 (오버라이드 하지 않는 한)
- identity → 왜 id가 같아야 하는가?
    - 테스트 일관성 (`is` 사용이 요구되는 경우) 을 위해 id 일관성이 필요한 경우 → `__eq__` 메서드를 정의함으로써 더 쉽게 실현 가능
    - mutable한 인스턴스를 딕셔너리의 키값으로 사용하기 위한 경우 → `__hash__` 메서드를 정의함으로써 fixed value를 얻을 수 있음
- behavior와 identity의 경우 unique instance가 아니어도 상관 없음 → 남은 건 **state(instance per state) →** 결국 ****singleton 패턴은 ****인스턴스들 간의 ****unique state을 달성하기 위해 사용
- Borg 패턴 → unique identity는 놔두고 unique state만 달성하도록 하자!

<br />

## vs Singleton 패턴

Borg 패턴은 복수의 인스턴스 생성이 가능 vs Singleton 패턴은 오직 하나의 인스턴스만 생성 가능 

✅ Monostate(Borg) forces a **behavior** (only one value along all class instances) 

✅ Singleton forces a **structural/creational constraint** (only one instance) 

- Borg 패턴은 인스턴스의 생성에 제약은 없지만 각각의 인스턴스의 state을 하나의 agent에 위임하도록 하는 행위의 제약이 걸려 있음 → **Behavioral** pattern
- Singleton은 인스턴스의 생성을 단 하나만 허용하도록 제한 → **Creational** Pattern

<br />

## vs Flyweight 패턴

- Flyweight 패턴이란 인스턴스들의 상태를 공유시켜 메모리 낭비를 줄이도록 하는 디자인 패턴
- Flyweight 패턴에서는 인스턴스 중 상태를 공유하지 않는 인스턴스가 있을 수 있지만, Borg 패턴에서는 다른 상태를 가지는 인스턴스가 생길 수 없음

<br />

## 프로젝트에서 적용해볼 수 있을 것 같은 부분 

**policy**
- 정책은 변하지 않는 부분
- 하나의 사항이 변경되면 다른 인스턴스들의 상태도 변경되어야 함


<br />
<br />

## 📚 Reference
- [https://youtu.be/Yj-4q17lZuc](https://youtu.be/Yj-4q17lZuc)
- [https://subscription.packtpub.com/book/application-development/9781783283378/2/ch02lvl1sec16/the-borg-singleton](https://subscription.packtpub.com/book/application-development/9781783283378/2/ch02lvl1sec16/the-borg-singleton)
- [http://www.aleax.it/Python/5ep.html](http://www.aleax.it/Python/5ep.html)
