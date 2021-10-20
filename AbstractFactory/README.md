# 추상 팩토리 패턴
→ 팩토리란? <br />
→ 팩토리 메서드 패턴이란? <br />
→ 팩토리 메서드 패턴과의 차이점은? <br />

<br />

## 1. 팩토리 메서드 패턴

*"The factory method pattern inserts <u>another layer/abstraction</u> between <u>instantiating an object</u> and <u>where in your code it is actually used</u>."*

### Concepts

1. Concrete Creator : Creator를 호출하는 클라이언트 (어플리케이션) 
2. Creator : Factory 메서드 → 객체를 생성 
3. Concrete Product : Factory로부터 만들어지는 클래스 혹은 객체
4. Product Interface : Concrete Product에 구현되어 있는 공통 인터페이스 (Common methods, attributes)

### Relationship

Concrete Creator→ access → Creator : 클라이언트는 새로운 객체를 얻기 위해 Factory 메서드에 접근  

Creator → return → Concrete Product : Factory 메서드가 객체를 반환

Concrete Product ← Implement ← Product Interface : 생성된 객체는 Product Interface를 구현

### Decode

*"The factory method pattern inserts <u>another layer/abstraction → Creator</u> between <u>instantiating an object → Concrete Product</u> and <u>where in your code it is actually used → Concrete Creator</u>."*

<br />

## 2. 추상 팩토리 패턴

*"A factory that can <u>return factories</u>"*

### vs 팩토리 메서드 패턴

팩토리 메서드 패턴 : 객체(Concrete Product)를 반환 

추상 팩토리 패턴 : 팩토리(Creator → Sub factories)를 반환

### Concepts

1. Client : 팩토리 메서드 패턴의 Concrete Creator → Abstract factory를 호출 
2. Abstract Factory : 서브 팩토리를 호출하는 팩토리 
3. Concrete Factory : Abstract Factory의 서브 팩토리 → Concrete Product의 Creator 
4. Concrete Product 
5. Abstract Product : Concrete Product가 구현하고 있는 Common Interface (Product Interface)

### Relationship

Client → access → Abstract Factory

Abstract Factory → access → Concrete Factory

 Concrete Factory → returns → Concrete Product 

Concrete Product ← Implement ← Abstract Product 

### Decode

*"<u>A factory → Abstract Factory</u> that can return <u>factories → Concrete Factory</u>"*

→ factory method pattern with more abstraction layer over related factories

<br />

## 3. Why use?

- 클라이언트에게 딱 필요한 만큼만의 정보를 제공
    
    → 나머지 정보 은폐 
    
    → 컴포넌트의 독립성 확보 
    
- **일관적인 의존성의 방향성 유지**
    - *"의존성 역전 원칙에서 말하는 '유연성이 극대화된 시스템'이란 소스 코드의 의존성이 추상에 의존하며 구체에는 의존하지 않는 시스템이다."* (클린 아키텍처, 92쪽)
    - 왜? 구체적인 요소는 변동성이 크기 때문 → 의존하고 있는 대상에 변동 사항이 생기면 거기에 의존하고 있던 모든 요소를 변경해야 함 → 개발 독립성 및 배포 독립성 확보 어려움
    - abstraction vs concretion → 추상 인터페이스에 변경 사항이 생기면 이를 구체화한 구현체들도 같이 수정해야 함. 반면 구현체에 변경이 생겨도 얘가 구현하고 있는 추상 인터페이스는 변경될 필요가 없음. 따라서 추상 인터페이스는 구체적인 구현체에 비해 변동성이 낮다.
    - 구체 함수나 객체는 소스 코드 의존성을 필요로 하고, 이를 직접 참조하게 되면 이 의존성을 상속받게 된다.
    - 따라서 일관적으로 변동성이 큰 구체적인 대상으로부터 변동성이 적인 추상적인 요소를 분리한 뒤, 소스 코드 의존성을 추상적인 쪽으로 일관되게 유지하기 위해 Abstract Factory를 사용하는 것.
    
    💬 의존성 역전 원칙 (Dependancy Inversion Principal) : 고수준의 정책을 구현하는 코드는 저수준의 세부 사항을 구현하는 코드에 절대로 의존해서는 안된다는 소프트웨어 설계 원칙


<br />

## 💬 ABC meta class란

*"Abstract Base Class"*

Product Interface를 구현하기 위한 developer tool

Interface를 제대로 구현하지 않았을 때의 에러를 보통은 런타임에서 잡게 되는데 ABC meta class를 사용함으로써 개발 단계에서 에러를 잡을 수 있음

<br />
<br />
<br />

## 📚 Reference

- [Abstract factory pattern with code examples](https://www.youtube.com/watch?v=TAnG6DN-5QM)
- [Abstract factory pattern](https://medium.com/design-patterns-in-python/abstract-factory-pattern-in-python-db1f949f6b7f)
- [ABC meta class](https://youtu.be/8HMurBw18wU)
- [클린 아키텍쳐 3부 11장 DIP: 의존성 역전 원칙 (로버트 마틴, 인사이트)](http://www.yes24.com/Product/Goods/77283734)
