public class DLList<bloop>{
	private Node sentinel;
	private int size;

	private class Node{
		public bloop item;
		public Node next;
		public Node prev;

		private Node(bloop x, Node nodenext, Node nodeprev){
			item = x;
			next = nodenext;
			prev = nodeprev;
		}
	}
	
	public DLList(){
		sentinel = new Node(null, null, null);
		sentinel.next = sentinel;
		sentinel.prev = sentinel; 
		size = 0; 
	}
	public void addfirst(bloop x){
		Node y = new Node(x, sentinel.next, sentinel);
		sentinel.next = y;
		y.next.prev = y;
		size += 1;	
	}
	public bloop getfirst(){
		return sentinel.next.item;
	}
	public bloop getlast(){
		return sentinel.prev.item;
	}
	public void addlast(bloop x){
		Node y = new Node(x, sentinel, sentinel.prev);
		Node temp = sentinel.prev;
		temp.next = y;
		sentinel.prev = y;
		size += 1;
	}
	public void removefirst(){
		sentinel.next = sentinel.next.next;
		sentinel.next.prev = sentinel;
		size -= 1;
	}
	public void removelast(){
		sentinel.prev = sentinel.prev.prev;
		sentinel.prev.next = null;
		size -= 1;
	}
	public int getsize(){
		return size;
	}
	public static void main(String[] args){
		DLList<Integer> s = new DLList<Integer>();
		s.addfirst(1);
		s.addfirst(2);
		s.addfirst(3);
		s.addlast(4);
		s.addlast(5);
		System.out.println(s.getfirst());
		System.out.println(s.getsize());
		s.removefirst();
		System.out.println(s.getfirst());
		System.out.println(s.getsize());
		s.removelast();
		System.out.println(s.getlast());
		System.out.println(s.getsize());
	}
}
